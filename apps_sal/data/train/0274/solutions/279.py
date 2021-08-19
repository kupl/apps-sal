class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sd = collections.deque()
        ld = collections.deque()

        def smallpush(d, i):
            while d and d[-1][0] > nums[i]:
                d.pop()
            d.append((nums[i], i))

        def largepush(d, i):
            while d and d[-1][0] < nums[i]:
                d.pop()
            d.append((nums[i], i))

        def popleft(d, j):
            while d and d[0][1] < j:
                d.popleft()
        n = len(nums)
        ans = -math.inf
        start = 0
        i = 0
        while i < n:
            smallpush(sd, i)
            largepush(ld, i)
            if abs(ld[0][0] - sd[0][0]) <= limit:
                ans = max(ans, i - start + 1)
            else:
                while abs(ld[0][0] - sd[0][0]) > limit:
                    if ld[0][1] == start:
                        ld.popleft()
                    if sd[0][1] == start:
                        sd.popleft()
                    start += 1
                ans = max(ans, i - start + 1)
            i += 1
        return ans

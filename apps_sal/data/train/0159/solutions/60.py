class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = collections.deque()
        result = nums[0]
        for i in range(n):
            while q and q[0][1] < i - k:
                q.popleft()
            a = q[0][0] if q else 0
            m = nums[i] + (a if a > 0 else 0)
            if m > 0:
                while q and m >= q[-1][0]:
                    q.pop()
                q.append((m, i))
            result = max(result, m)
        return result

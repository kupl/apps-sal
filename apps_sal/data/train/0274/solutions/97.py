class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        asc, desc = deque(), deque()
        left = 0
        longest = 0
        for i, n in enumerate(nums):
            if not asc:
                asc.append([n, i])
            else:
                while asc and asc[-1][0] > n:
                    asc.pop()
                asc.append([n, i])
            if not desc:
                desc.append([n, i])
            else:
                while desc and desc[-1][0] < n:
                    desc.pop()
                desc.append([n, i])

            while desc[0][0] - asc[0][0] > limit:
                if desc[0][1] < asc[0][1]:
                    left = desc.popleft()[1] + 1
                else:
                    left = asc.popleft()[1] + 1

            longest = max(longest, i - left + 1)

        return longest

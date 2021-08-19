class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        w_start = 0
        d = {}
        max_len = 0
        case = 0
        for i in range(0, len(nums)):
            c = str(nums[i])
            if c not in d:
                d[c] = 0
            d[c] += 1
            if str(0) in d:
                while d[str(0)] > 1:
                    t = str(nums[w_start])
                    d[t] -= 1
                    w_start += 1
                    case = 1
            max_len = max(max_len, i - w_start + 1 - case)
            case = 0
        return max_len - 1

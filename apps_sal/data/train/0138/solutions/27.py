class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # DP may be unnecessary, but because I saw max length subarray
        # I assumed that it would be DP. Solution approach was DP-esque
        # but it doesn't seem necessary.
        # Seems like another way could be to just count the number of
        # negatives (between 0s).
        p = 0
        n = 0
        longest_p = 0
        for num in nums:
            longest_p = max(longest_p, p)
            if num == 0:
                p = 0
                n = 0
            elif num > 0:
                prev_p = p
                prev_n = n
                p = prev_p + 1
                if prev_n > 0:
                    n = prev_n + 1
                else:
                    n = 0
            elif num < 0:
                prev_p = p
                prev_n = n
                n = prev_p + 1
                if prev_n > 0:
                    p = prev_n + 1
                else:
                    p = 0
        longest_p = max(longest_p, p)
        return longest_p

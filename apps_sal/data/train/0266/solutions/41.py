class Solution:
    def numSplits(self, s: str) -> int:
        left_count = collections.Counter()
        right_count = collections.Counter(s)
        ans = 0
        for ch in s:
            left_count[ch] += 1
            right_count[ch] -= 1
            if right_count[ch] == 0:
                del right_count[ch]
            
            if len(left_count) == len(right_count):
                ans += 1
        return ans

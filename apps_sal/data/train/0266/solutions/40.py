class Solution:

    def numSplits(self, s: str) -> int:
        counter = 0
        left = defaultdict(int)
        right = defaultdict(int)
        for c in s:
            right[c] += 1
        for i in range(len(s)):
            left[s[i]] += 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            if len(left.keys()) == len(right.keys()):
                counter += 1
        return counter

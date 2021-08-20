class Solution:

    def numSplits(self, s: str) -> int:
        if not s or len(s) < 0:
            return 0
        right = {}
        left = {s[0]: 1}
        count = 0
        if len(left) == len(right):
            count += 1
        for i in range(1, len(s)):
            if s[i] in right:
                right[s[i]] += 1
            else:
                right[s[i]] = 1
        if len(left) == len(right):
            count += 1
        for i in range(1, len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
            if s[i] in left:
                left[s[i]] += 1
            else:
                left[s[i]] = 1
            if len(left) == len(right):
                count += 1
        return count

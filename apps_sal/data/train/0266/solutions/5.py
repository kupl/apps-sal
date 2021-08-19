class Solution:

    def numSplits(self, s: str) -> int:
        count = 0
        left = set(s[:1])
        right = set(s[1:])
        if len(left) == len(right):
            count += 1
        k = 0
        for i in range(1, len(s)):
            if s[i] not in left:
                left.add(s[i])
            if s[i] not in s[i + 1:]:
                k += 1
            diff = len(left) - (len(right) - k)
            if diff == 0:
                count += 1
            elif diff > 0:
                break
        return count

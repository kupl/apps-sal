class Solution:
    def numSplits(self, s: str) -> int:
        left_unique = [0 for x in range(len(s))]
        right_unique = [0 for x in range(len(s))]
        left_set = set()
        right_set = set()
        for x in range(len(s)):
            if s[x] not in left_set:
                left_set.add(s[x])
                if x > 0:
                    left_unique[x] = left_unique[x - 1] + 1
                else:
                    left_unique[x] += 1
            else:
                left_unique[x] = left_unique[x - 1]
            if s[len(s) - 1 - x] not in right_set:
                right_set.add(s[len(s) - x - 1])
                if x > 0:
                    right_unique[len(s) - x - 1] = right_unique[len(s) - x] + 1
                else:
                    right_unique[len(s) - x - 1] += 1
            else:
                right_unique[len(s) - x - 1] = right_unique[len(s) - x]

        min_splits = 0
        for x in range(1, len(s)):
            if left_unique[x - 1] == right_unique[x]:
                min_splits += 1
        return min_splits

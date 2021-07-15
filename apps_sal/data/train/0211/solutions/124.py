class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        for count in range(len(s)):
            for partitions in combinations(range(1, len(s)), count):
                partitions = [0] + list(partitions) + [len(s)]
                parts = [s[a:b] for a, b in zip(partitions, partitions[1:])]
                if len(parts) == len(set(parts)):
                    res = max(res, len(parts))
        return res

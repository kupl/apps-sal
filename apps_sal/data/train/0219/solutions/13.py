class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        n = len(hours)
        hashmap = dict()
        total = 0
        res = 0

        for i in range(n):
            if hours[i] <= 8:
                total -= 1
            else:
                total += 1

            if total > 0:
                res = i + 1
                continue
            else:
                if total not in hashmap:
                    hashmap[total] = i
                if (total - 1) in hashmap:
                    res = max(res, i - hashmap[total - 1])
        return res

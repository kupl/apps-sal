class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        d = {}
        d[0] = -1
        res = 0
        for i in range(len(hours)):
            hours[i] = (1 if hours[i] > 8 else -1) + (0 if i == 0 else hours[i - 1])
            if hours[i] not in d:
                d[hours[i]] = i
            if hours[i] > 0:
                res = i + 1
            target = hours[i] - 1
            if target in d:
                res = max(res, i - d[target])
        print(hours)
        print(d)
        return res

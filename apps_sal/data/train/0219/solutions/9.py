class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        d = {}
        P = [0] #prefix sum
        F = [0 for i in range(len(hours))]
        res = 0
        for i in range(len(hours)):
            P.append(P[-1] + (1 if hours[i] > 8 else -1))
            if P[-1] > 0:
                F[i] = i + 1
            else:
                s = d.get(P[-1] - 1, -1)
                if s >= 0:
                    F[i] = max(F[i], i - s + F[s])
            if P[-1] not in d:
                d[P[-1]] = i
            res = max(res, F[i])   

        return res

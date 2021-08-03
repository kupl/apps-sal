class Solution:
    def countTriplets(self, A: List[int]) -> int:
        t = 0
        d = {}
        for i in A:
            for j in A:
                a = i & j
                if a in d:
                    d[a] += 1
                else:
                    d[a] = 1
        for k in d:
            for i in A:
                if k & i == 0:
                    t += d[k]
        return t

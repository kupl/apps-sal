class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        possibilities = []
        for k in range(1, N):
            comb = itertools.combinations(list(range(1, N)), k)
            possibilities += [[s[0:x[0]]] + [s[x[i]:x[i + 1]] for i in range(len(x) - 1)] + [s[x[-1]:]] for x in comb]
        ansr = 1
        for k in possibilities:
            if len(k) == len(set(k)):
                ansr = max(ansr, len(k))
        return ansr

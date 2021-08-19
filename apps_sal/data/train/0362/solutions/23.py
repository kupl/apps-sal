class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        k = len(hats)
        persons = defaultdict(list)
        for (i, hs) in enumerate(hats):
            for h in hs:
                persons[h].append(i)
        dic = defaultdict(int)
        dic[0] = 1
        for (hat, ps) in persons.items():
            nex = dic.copy()
            for mask in dic:
                for p in ps:
                    if mask >> p & 1 == 0:
                        nex[mask | 1 << p] = (nex[mask | 1 << p] + dic[mask]) % mod
            dic = nex
        return dic[(1 << k) - 1]

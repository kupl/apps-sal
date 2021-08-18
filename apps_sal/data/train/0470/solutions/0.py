class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        counter = collections.Counter(A)
        i, res, l, ckey = 0, 0, len(counter), sorted(list(counter.keys()))
        if target % 3 == 0:
            res += math.comb(counter[target // 3], 3)
        for i in range(l):
            ni = ckey[i]
            nk = target - (2 * ni)
            if ni != nk and nk >= 0:
                res += math.comb(counter[ni], 2) * counter[nk]
        for i in range(l):
            for j in range(i + 1, l):
                ni, nj = ckey[i], ckey[j]
                nk = target - ni - nj
                if ni < nj < nk <= 100:
                    res += counter[ni] * counter[nj] * counter[nk]
        return res % (10**9 + 7)

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        counter = collections.Counter(A)
        i, res, l, ckey = 0, 0, len(counter), sorted(list(counter.keys()))
        print(counter)
        print((l // 2))
        if target % 3 == 0:
            res += math.comb(counter[target // 3], 3)
            print((target // 3, target // 3, target // 3, res))
        for i in range(l):
            ni = ckey[i]
            nk = target - (2 * ni)
            if ni != nk and nk >= 0:
                res += math.comb(counter[ni], 2) * counter[nk]
            print((ni, ni, nk, res))
        for i in range(l):
            for j in range(i + 1, l):
                ni, nj = ckey[i], ckey[j]
                nk = target - ni - nj
                if ni < nj < nk <= 100:
                    res += counter[ni] * counter[nj] * counter[nk]
                print((ni, nj, nk, res))
        return res % (10**9 + 7)
        # while i < l:
        #     j = i
        #     while j < l:
        #         ni, nj = ckey[i], ckey[j]
        #         nk = target - ni - nj
        #         if ni == nk == nj:
        #             res += math.comb(counter[ni], 3)
        #         elif nj == nk:
        #             res += math.comb(counter[nj], 2) * counter[ni]
        #         elif ni == nk:
        #             res += math.comb(counter[nk], 2) * counter[nj]
        #         elif ni == nj:
        #             res += math.comb(counter[ni], 2) * counter[nk]
        #         else:
        #             res += counter[ni] * counter[nj] * counter[nk]
        #         print(ni, nj, nk, res)
        #         j += 1
        #     i += 1
        # return res % (10**9 + 7)

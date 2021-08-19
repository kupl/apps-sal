class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # piles = sorted(piles)
        # while piles:
        #     piles.pop(-1)
        #     res += piles.pop(-1)
        #     piles.pop(0)
        min_, max_ = min(piles), max(piles)

        cnt = [0 for i in range(min_, max_ + 1)]

        res = []
        v = 0
        for i in range(len(piles)):
            cnt[piles[i] - min_] += 1

        for i in range(len(cnt)):
            while cnt[i] > 0:
                res.append(i + min_)
                cnt[i] -= 1
        res = res[::-1]
        round_ = len(piles) // 3
        end = len(piles) - round_
        for i in res[1:end:2]:
            v += i

        return v

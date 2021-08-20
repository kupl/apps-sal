class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        rec = [0] * amount
        fr = [0]
        new = []
        l = 1
        while fr or new:
            if not fr:
                fr = new
                new = []
                l += 1
            cur = fr.pop(0)
            for c in coins:
                if cur + c == amount:
                    return l
                if cur + c < amount and (not rec[cur + c]):
                    new.append(cur + c)
                    rec[cur + c] = 1
        return -1

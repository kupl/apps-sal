class Solution:

    def numDupDigitsAtMostN(self, N: int) -> int:
        if N < 100:
            return N // 11
        s = str(N)
        l = len(s)
        if l > 10:
            return N - 8877690
        mapping = {0: 0, 1: 9, 2: 90, 3: 738, 4: 5274, 5: 32490, 6: 168570, 7: 712890, 8: 2345850, 9: 5611770, 10: 8877690}
        seen = set()
        for (i, d) in enumerate(s):
            d = int(d)
            if d > 0:
                f = sum((1 for j in range(1 if i == 0 else 0, d) if j not in seen))
                for j in range(l - i - 1):
                    f *= 9 - i - j
                N -= f
            if i == l - 1 and d not in seen:
                N -= 1
            if d in seen:
                break
            seen.add(d)
        return N - mapping[l - 1]

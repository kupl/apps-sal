class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = [0] * 999999

        for num in range(lo, hi + 1):
            if cache[num] != 0:
                continue

            path = [num]

            while num != 1 and cache[num] == 0:
                if num % 2 == 0:
                    num //= 2
                    path.append(num)
                else:
                    num = num * 3 + 1
                    path.append(num)

            for idx, n in enumerate(path):
                if cache[n] != 0:
                    break
                cache[n] = len(path) - 1 - idx + cache[path[-1]]

        res = [(i + lo, steps) for i, steps in enumerate(cache[lo:hi + 1])]
        res = sorted(res, key=lambda _: _[1])
        return res[k - 1][0]

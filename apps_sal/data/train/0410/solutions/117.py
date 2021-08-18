class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def find_transform(x):
            k = [x]
            while k[-1] != 1:
                if x % 2 == 0:
                    x = x / 2
                    k.append(x)
                else:
                    x = x * 3 + 1
                    k.append(x)
            return len(k) - 1
        power = []
        for i in range(lo, hi + 1):
            power.append([i, find_transform(i)])
        return sorted(power, key=lambda x: x[1])[k - 1][0]

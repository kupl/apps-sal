class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = []
        f.append(1)
        f.append(1)
        while 1:
            if max(f) <= k:
                f.append(f[len(f) - 1] + f[len(f) - 2])
            else:
                break
        f.remove(f[len(f) - 1])

        number = 0
        while k != 0:
            if f[len(f) - 1] <= k:
                k -= f[len(f) - 1]
                f.remove(max(f))
                number += 1
            else:
                f.remove(max(f))

        return number

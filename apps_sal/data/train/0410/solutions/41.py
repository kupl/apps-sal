class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []

        def power(x):
            count = 0
            while(x != 1):
                if (x % 2 == 0):
                    x = x // 2
                    count += 1
                elif(x % 2 != 0):
                    x = 3 * x + 1
                    count += 1
            return count
        for i in range(lo, hi + 1):
            p = power(i)
            arr.append((i, p))
        arr = [j[0] for j in sorted(arr, key=lambda x: x[1])]
        return arr[k - 1]

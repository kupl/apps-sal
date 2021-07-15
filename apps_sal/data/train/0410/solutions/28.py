class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        for i in range(lo, hi + 1):
            counter = 0
            num = i
            while num != 1:
                if num % 2 == 1:
                    num = 3 * num + 1
                else:
                    num = num // 2
                counter += 1
            arr.append([i, counter])
        arr.sort()
        for i in arr:
            i[0], i[1] = i[1], i[0]
        arr.sort()
        return arr[k - 1][1]

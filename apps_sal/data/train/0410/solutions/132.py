class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def collatz(num, moves=0):
            if num == 1:
                return moves
            if num % 2 == 0:
                return collatz(num / 2, moves + 1)
            else:
                return collatz(num * 3 + 1, moves + 1)
        arr = [(i, collatz(i)) for i in range(lo, hi + 1)]
        arr.sort(key=lambda x: x[1])
        print(arr)
        return arr[k - 1][0]

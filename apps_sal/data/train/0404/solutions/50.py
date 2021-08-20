class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        self.arr = [[None for i in range(K)] for i in range(len(A))]
        res = self.solve(A, 0, K, -1)
        return res

    def solve(self, arr, i, grpLeft, lastInd):
        if i == len(arr):
            return 0
        if self.arr[lastInd + 1][grpLeft - 1] != None:
            return self.arr[lastInd + 1][grpLeft - 1]
        if grpLeft == 1:
            self.arr[lastInd + 1][0] = sum(arr[lastInd + 1:]) / (len(arr) - lastInd - 1)
            return self.arr[i][0]
        avg = float(sum(arr[lastInd + 1:i + 1])) / (i - lastInd)
        self.arr[lastInd + 1][grpLeft - 1] = max(self.solve(arr, i + 1, grpLeft, lastInd), avg + self.solve(arr, i + 1, grpLeft - 1, i))
        return self.arr[lastInd + 1][grpLeft - 1]

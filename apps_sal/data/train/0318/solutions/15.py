class Solution:

    def __init__(self):
        self.dp = {}

    def solve_linear(self, slices, ind, to_choose):
        if (ind, to_choose) not in self.dp:
            N = len(slices)
            if N <= ind or to_choose == 0:
                return 0
            result_choose = self.solve_linear(slices, ind + 2, to_choose - 1)
            result_not_choose = self.solve_linear(slices, ind + 1, to_choose)
            self.dp[(ind, to_choose)] = max(result_choose + slices[ind], result_not_choose)
        return self.dp[(ind, to_choose)]

    def maxSizeSlices(self, slices: List[int]) -> int:
        min_elem = min(slices)
        min_ind = 0
        while slices[min_ind] != min_elem:
            min_ind += 1
        N = len(slices)
        min_ind += 1
        arr = [0 for _ in range(N)]
        for i in range(N):
            arr[i] = slices[(min_ind + i) % N]
        return self.solve_linear(arr, 0, int(N / 3))

class Solution:

    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append(2 * i + 1)
        double_cnt = 0
        for i in range(len(arr)):
            double_cnt += abs(arr[i] - n)
        return double_cnt // 2

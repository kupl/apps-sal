class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        base = 10 ** 9 + 7
        if all([x >= 0 for x in arr]):
            return sum(arr) * k
        if all([x <= 0 for x in arr]):
            return 0
        sol1 = self.maxsub(arr)
        sol2 = self.maxsub(arr + arr)
        (ma, mi) = (0, 0)
        presum = 0
        i = 0
        while i < len(arr):
            presum += arr[i]
            if presum > ma:
                ma = presum
            elif presum < mi:
                mi = presum
            i += 1
        if sum(arr) > 0:
            sol3 = max(ma + sum(arr) * (k - 1), sum(arr) * k - mi)
            sol2 = sol2 + (k - 2) * sum(arr)
            return max(sol1, sol2, sol3) % base
        return max(sol1, sol2) % base

    def maxsub(self, arr):
        sol = 0
        temp = 0
        i = 0
        while i < len(arr):
            temp += arr[i]
            if temp < 0:
                temp = 0
            else:
                sol = max(sol, temp)
            i += 1
        return sol

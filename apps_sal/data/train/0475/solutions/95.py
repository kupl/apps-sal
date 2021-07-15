MODULO = 10**9 + 7

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(num + prefix_sums[-1])
        
        sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sums.append(prefix_sums[j] - prefix_sums[i])
        
        sums.sort()
        summa = 0
        for i in range(left-1, right):
            summa = (summa + sums[i]) % MODULO
        return summa

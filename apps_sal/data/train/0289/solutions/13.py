class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        dpA = self.sumArray(A, L)
        dpB = self.sumArray(A, M)
        print(dpA)
        print(dpB)
        max_v = 0
        for i in range(len(dpA)):
            for m in range(len(dpB)):
                if m >= i and m - i < L:
                    continue
                if i >= m and i - m < M:
                    continue
                max_v = max(max_v, dpA[i] + dpB[m])
        return max_v
        
        
    def sumArray(self, lst, length):
        result = []
        for i in range(len(lst) - length + 1):
            sub_sum = lst[i]
            for m in range(1, length):
                sub_sum += lst[i + m]
            result.append(sub_sum)
        return result

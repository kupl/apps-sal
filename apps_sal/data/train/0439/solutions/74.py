class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        maxAB, currA, currB = 1, 1, 1  # 初始化

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:  # 以第 i 个元素结尾，呈现升序的情况
                currA = currB + 1
                currB = 1
            elif A[i] < A[i - 1]:  # 以第 i 个元素结尾，呈现降序的情况
                currB = currA + 1
                currA = 1
            else:
                currA, currB = 1, 1  # 出现相等的情况，重新计数

            maxAB = max(maxAB, currA, currB)  # 更新最优值

        return maxAB


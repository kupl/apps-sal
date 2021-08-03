class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        ans = 0
        setA = set(A)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                temp = 2
                x = A[j]
                y = A[i] + A[j]
                while y in setA:
                    temp += 1
                    x, y = y, x + y
                ans = max(ans, temp)

        return ans if ans >= 3 else 0

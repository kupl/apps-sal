class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        result = 0
        from collections import Counter
        d = Counter(A)
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                (x, y) = (A[i], A[j])
                temp = 0
                while d[x + y] != 0:
                    (x, y) = (y, x + y)
                    temp += 1
                result = max(result, temp)
        print(result + 2)
        return result + 2 if result > 0 else 0

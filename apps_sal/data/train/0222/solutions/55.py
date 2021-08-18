class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        res = 0
        A_dict = {}
        for x in A:
            A_dict[x] = A_dict.get(x, 0) + 1

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                c = a + b
                length = 0
                while c in A_dict:
                    length += 1
                    a, b = b, c
                    c = a + b
                res = max(res, length)

        return res + 2 if res > 0 else 0

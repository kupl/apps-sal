class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:

        def getFS(x1, x2):
            F = [x1, x2]
            while F[-1] <= 1000000000:
                F.append(F[-2] + F[-1])
            return F
        C1 = getFS(1, 0)
        C2 = getFS(0, 1)

        def getLLFS(start, x1, x2):
            max_len = 2
            F = [x1, x2]
            xi = x1 + x2
            for i in range(start, len(A)):
                if A[i] == xi:
                    max_len += 1
                    F.append(xi)
                    xi = F[-2] + F[-1]
            return max_len
        if len(A) < 3:
            return len(A)
        max_len = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                (x1, x2) = (A[i], A[j])
                last = x1 * C1[max_len - 1] + x2 * C2[max_len - 1]
                if last > A[-1]:
                    break
                max_len = max(max_len, getLLFS(j + 1, x1, x2))
        if max_len < 3:
            return 0
        return max_len

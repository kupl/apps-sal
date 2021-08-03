class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(set(A)) == 1:
            return 1
        a, b = (1, -1)[A[0] < A[1]], (1, -1)[A[-1] > A[-2]]
        A.extend([A[-1] + a, A[0] - b])
        A[0], A[1:] = A[-1], A[0:-1]
        ct = 0
        totalct = []
        i = 1
        while i < len(A) - 1:
            a, b, c = A[i - 1], A[i], A[i + 1]
            if (b > a) == (b > c) and b not in [a, c]:
                ct += 1
            else:
                if ct + 1 == i:
                    totalct.append(ct + 1)
                else:
                    totalct.append(ct + 2)
                ct = 0
            i += 1
        if totalct:
            ct += 1
        totalct.append(ct)
        return max(totalct)

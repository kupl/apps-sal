class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        mem = dict()

        def process(A, B):
            key = '%s_%s' % (A, B)

            if A == B:
                return 0

            if key in mem:
                return mem[key]

            if A[0] == B[0]:
                return process(A[1:], B[1:])

            c2 = float('inf')
            temp = list(B)

            for idx, val in enumerate(B):
                if val == A[0]:
                    temp[idx], temp[0] = temp[0], temp[idx]
                    c2 = min(c2, 1 + process(A[1:], ''.join(temp)[1:]))
                    temp[0], temp[idx] = temp[idx], temp[0]

            mem[key] = c2
            return mem[key]

        return process(A, B)

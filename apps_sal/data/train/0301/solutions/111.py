class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        N_a = len(A)
        N_b = len(B)
        pair2maxlines = defaultdict(int)

        def max_lines(a, b):
            if pair2maxlines.get((a, b)) is None:
                if a == N_a or b == N_b:
                    pair2maxlines[a, b] = 0
                    return 0
                if A[a] == B[b]:
                    output = 1 + max_lines(a + 1, b + 1)
                    pair2maxlines[a, b] = output
                    return output
                output = max(max_lines(a + 1, b), max_lines(a, b + 1))
                pair2maxlines[a, b] = output
                return output
            else:
                return pair2maxlines[a, b]
        return max_lines(0, 0)

class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        cnt
        arith = [Counter() for i in range(len(A))]
        for i in range(len(A) - 2, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                arith[i][diff] = max(1 + arith[j][diff], arith[i][diff])
        longest = 0
        for i in range(len(A)):
            most_common = arith[i].most_common()
            longest = max(most_common[0][1] if most_common else 0, longest)
        return longest + 1

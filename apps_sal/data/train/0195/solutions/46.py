class Solution:

    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        C = defaultdict(int)
        for i in range(n):
            C[A[i]] += 1
            for j in range(i + 1, n):
                C[A[i] & A[j]] += 2
        return sum((c * sum((x & y == 0 for y in A)) for (x, c) in C.items()))

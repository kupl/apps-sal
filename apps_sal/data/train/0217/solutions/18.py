class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        S, last = set(), set()
        for i in range(len(A)):
            last = {a | A[i] for a in last}
            last.add(A[i])
            S |= last

        return len(S)

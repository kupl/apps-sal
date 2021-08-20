class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        if not A:
            return []
        for i in range(len(A))[::-1]:
            if i > 0 and A[i] == A[i - 1]:
                A.pop(i)
        all_outcomes = set()
        outcomes = set()
        for elt in A:
            outcomes = {elt} | {elt | val for val in outcomes}
            all_outcomes |= outcomes
        return len(all_outcomes)

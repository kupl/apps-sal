class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        if not A:
            return []
        for i in range(len(A))[::-1]:
            if i > 0 and A[i] == A[i - 1]:
                A.pop(i)
        all_outcomes = set([A[0]])
        outcomes = set([A[0]])
        for elt in A[1:]:
            temp = set([elt])
            for out in outcomes:
                temp.add(out | elt)
            outcomes = temp
            all_outcomes |= outcomes
        return len(all_outcomes)

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:

        if not A:
            return []

        all_outcomes = set()
        outcomes = set()
        for elt in A:
            outcomes = {elt} | {elt | val for val in outcomes}
            all_outcomes |= outcomes

        return len(all_outcomes)

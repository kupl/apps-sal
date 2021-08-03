class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = collections.Counter(ages)
        def valid(A, B): return not any([A * .5 + 7 >= B, A < B, A < 100 < B])
        count = 0

        items = list(counts.items())
        for A, cntA in items:
            for B, cntB in items:
                if valid(A, B):
                    count += cntA * cntB
                    if A == B:
                        count -= cntA

        return count

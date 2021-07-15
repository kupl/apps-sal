from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # Brute Force with Set
        # Time  complexity: O(N^2 x logM), where N is the length of A, 
        # and M is the maximum value of A.
        # Space complexity: O(N)
        # S, ans = set(A), 0
        # for i in range(len(A)):
        #     for j in range(i + 1, len(A)):
        #         x, y, l = A[j], A[i] + A[j], 2
        #         while y in S:
        #             x, y = y, x + y
        #             l += 1
        #         ans = max(ans, l)
        # return ans if ans >= 3 else 0


        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(NlogM), where M is the largest element of A.
        index = {x: i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0


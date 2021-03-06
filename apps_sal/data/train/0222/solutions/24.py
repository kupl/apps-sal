class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for (i, x) in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        result = 0
        for (k, z) in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], len(A) + 1)
                if i < j:
                    longest[j, k] = longest[i, j] + 1
                    if longest[j, k] > result:
                        result = longest[j, k]
        return result if result >= 3 else 0

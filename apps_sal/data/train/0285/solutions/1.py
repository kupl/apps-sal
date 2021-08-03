class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()

        minA = A[0]
        maxA = A[-1]

        smallest = maxA - minA

        for i in range(len(A) - 1):
            a = A[i]
            b = A[i + 1]

            smallest = min(smallest, max(maxA - K, a + K) - min(minA + K, b - K))

        return smallest

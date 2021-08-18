class Solution:
    def maxEqualFreq(self, A: List[int]) -> int:
        n = len(A)
        count = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        for i in range(n):
            count[A[i]] += 1
            freq[count[A[i]]] += 1

        for i in range(n - 1, 0, -1):
            if count[A[i]] * freq[count[A[i]]] == i:
                return i + 1
            freq[count[A[i]]] -= 1
            count[A[i]] -= 1
            if count[A[i - 1]] * freq[count[A[i - 1]]] == i:
                return i + 1

        return 1

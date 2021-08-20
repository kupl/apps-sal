class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        longest = 0
        coll = set(A)
        n = len(A)
        target = [[None for _ in range(n)] for _ in range(n)]
        lookup = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                target[i][j] = A[i] + A[j]
                prev = A[j]
                while target[i][j] in coll:
                    if lookup[i][j]:
                        lookup[i][j] += 1
                    else:
                        lookup[i][j] = 3
                    temp = target[i][j]
                    target[i][j] += prev
                    prev = temp
                    longest = max(longest, lookup[i][j])
        return longest

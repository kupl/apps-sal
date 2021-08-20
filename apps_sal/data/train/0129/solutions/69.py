class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        return self.with_sort(A)

    def with_sort(self, A):
        n = len(A)
        max_list = [(i[0] + i[1], i[0]) for i in sorted(enumerate(A), key=lambda x: -(x[1] + x[0] * 1.000000001))]
        idx = 0
        max_s = 0
        for j in range(n - 1, -1, -1):
            s = A[j] - j
            while idx < n and max_list[idx][1] >= j:
                idx += 1
            if idx < n:
                s += max_list[idx][0]
            max_s = max(max_s, s)
        return max_s

    def count_sort(self, A):
        C = [[] for _ in range(51001)]
        for (i, a) in enumerate(A):
            C[a + i].append((a + i, i))
        res = []
        k = 0
        for c in C:
            if len(c) > 0:
                res.extend(c)
        return list(reversed(res))

    def brute_force(self, A):
        max_score = 0
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                s = A[i] + A[j] + i - j
                if s > max_score:
                    max_score = s
        return max_score

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)

        dp = collections.defaultdict(int)

        ret = 0

        a_set = set(A)

        for i in range(n):
            for j in range(i + 1, n):
                dp[(A[i], A[j])] = 2

                left = A[j] - A[i]

                if left >= A[i] or left not in a_set:
                    continue

                #print(left, A[i], A[j], dp[(left, A[i])])

                dp[(A[i], A[j])] = dp[(left, A[i])] + 1

                ret = max(ret, dp[(A[i], A[j])])

        return ret

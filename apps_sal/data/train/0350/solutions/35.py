class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        # Important
        # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

        print((self.atmost_counts(A, K), self.atmost_counts(A, K - 1)))
        return self.atmost_counts(A, K) - self.atmost_counts(A, K - 1)

    def atmost_counts(self, A, K):

        counter = collections.Counter()

        res = i = 0

        for j in range(len(A)):

            if counter[A[j]] == 0:
                K -= 1

            counter[A[j]] += 1

            while K < 0:
                counter[A[i]] -= 1
                if counter[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res

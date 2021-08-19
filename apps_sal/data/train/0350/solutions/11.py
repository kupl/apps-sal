from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        """
        1 2 1 2 3
        i       j

        2 1 1 1 2
        i j
        """
        N = len(A)

        def atMost(k):
            if k == 0:
                return 0
            ret = i = j = 0
            cnt = Counter()
            while i < N:
                x = A[i]
                while j < N and (len(cnt) < k or A[j] in cnt):
                    cnt[A[j]] += 1
                    j += 1
                ret += j - i
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                i += 1
            return ret
        return atMost(K) - atMost(K - 1)

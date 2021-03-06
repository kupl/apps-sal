class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        result = 0
        (i, j) = (0, 0)
        cnt = collections.Counter()
        l = 0
        n = len(A)
        while j < n:
            if len(cnt) != K:
                cnt[A[j]] += 1
                if len(cnt) == K:
                    l = 1
                    while cnt[A[i]] > 1:
                        cnt[A[i]] -= 1
                        i += 1
                        l += 1
                    result += l
            elif A[j] in cnt:
                cnt[A[j]] += 1
                while cnt[A[i]] > 1:
                    cnt[A[i]] -= 1
                    i += 1
                    l += 1
                result += l
            else:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    cnt.pop(A[i])
                cnt[A[j]] += 1
                i += 1
                l = 1
                while cnt[A[i]] > 1:
                    cnt[A[i]] -= 1
                    i += 1
                    l += 1
                result += l
            j += 1
        return result

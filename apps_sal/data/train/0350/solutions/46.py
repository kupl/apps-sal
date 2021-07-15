class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:        
        def atMostK(A, K):
            ans, curr = 0, 0
            cnt = defaultdict(int)
            i = 0
            for j, num in enumerate(A):
                if num not in cnt:
                    K -= 1
                cnt[num] += 1
                while K<0:
                    cnt[A[i]] -= 1
                    if cnt[A[i]] == 0:
                        del cnt[A[i]]
                        K += 1
                    i += 1
                ans += j - i + 1
            return ans
        return atMostK(A, K) - atMostK(A, K-1)


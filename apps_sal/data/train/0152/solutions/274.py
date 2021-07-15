class Solution:
    def maxDistance(self, A, m: int) -> int:
        
        
        A.sort()
        
        def test(mid):
            cnt = m - 1
            cur = A[0]
            for i in A[1:]:
                if i - cur >= mid:
                    cnt -= 1
                    cur = i
                else:
                    continue
                if cnt == 0: return True
            return False
        
        mi = 1
        ma = (A[-1] - A[0]) // (m - 1)
        while mi <= ma:
            mid = (mi + ma) // 2
            if test(mid):
                mi = mid + 1
            else:
                ma = mid - 1
        return ma

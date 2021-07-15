#https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/854038/Beginner-Friendly-solution-or-Explained-with-time-complexity-analysis
    
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def check(dist):
            prev = position[0]
            cnt = 1
            idx = 0
            while idx<len(position):
                curr = position[idx]
                if curr-prev>=dist:
                    cnt += 1
                    prev = curr
                idx += 1
                if cnt>m:
                    break
            return cnt
        
        position.sort()
        L = 1
        R = position[-1]-position[0]
        
        while L<R:
            # print ('a ', L, R)
            if L==R-1:
                if check(R)>=m:
                    return R
                else:
                    return L
            mid = L+(R-L)//2
            if check(mid)<m:
                R = mid-1
            else:
                L = mid
            # print (L, R)
        return L

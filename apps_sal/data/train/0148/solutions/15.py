import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m,n={},len(difficulty)
        for ind, val in enumerate(difficulty):
            m[val]=max(m.get(val,0),profit[ind])
        difficulty.sort()
        for ind, val in enumerate(difficulty):
            if ind>0:
                m[val]=max(m[val],m[difficulty[ind-1]])
        
        ans = 0
        for ind, val in enumerate(worker):
            d_ind = bisect.bisect_left(difficulty, val)
            if d_ind<n:
                if difficulty[d_ind]<=val:
                    ans+=m[difficulty[d_ind]]
                else:
                    ans+=m[difficulty[d_ind-1]] if d_ind>0 else 0
            else:
                ans+=m[difficulty[d_ind-1]]
        return ans


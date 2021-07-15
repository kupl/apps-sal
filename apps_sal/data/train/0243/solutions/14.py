class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad=[]
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                bad.append(fronts[i])

        ans=10000000000
        for i in range(len(fronts)):
            if fronts[i] not in bad:
                ans=min(ans,fronts[i])
            if backs[i] not in bad:
                ans=min(ans, backs[i])
        if ans>0 and ans!=10000000000:
            return ans
        return 0


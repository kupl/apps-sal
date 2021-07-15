class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans=set()
        vset=set()
        for a in A:
            newvset=set()
            for v in vset:
                newvset.add(a|v)
                ans.add(a|v)
            newvset.add(a)
            vset=newvset
            ans.add(a)
        return len(ans)


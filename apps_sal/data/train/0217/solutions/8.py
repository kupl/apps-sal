class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans=set()
        cur=set()
        for i in A:
            cur = set([i|j for j in cur])
            cur.add(i)
            ans|=cur
        return len(ans)

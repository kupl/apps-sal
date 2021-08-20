class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set(A)
        prev = set([A[0]])
        for i in A[1:]:
            temp = set()
            for p in prev:
                temp.add(i | p)
                ans.add(i | p)
            prev = temp
            prev.add(i)
        return len(ans)

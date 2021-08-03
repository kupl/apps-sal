class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        prev = set()
        prev.add(0)

        for i in range(len(A)):
            cur = set()
            cur.add(A[i])

            for p in prev:
                res = p | A[i]
                if res != p:
                    ans.add(p)
                cur.add(res)

            prev = cur

        for p in prev:
            ans.add(p)

        if 0 not in A:
            ans.remove(0)

        return len(ans)

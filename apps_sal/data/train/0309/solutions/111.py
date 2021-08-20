class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)
        onleft = set()
        onright = [0 for _ in range(501)]
        toextend = [{} for _ in range(501)]
        res = 2
        for v in A:
            onright[v] += 1
        for i in range(0, length):
            val = A[i]
            tex = toextend[val]
            onright[val] -= 1
            for lval in onleft:
                diff = val - lval
                nextval = val + diff
                if nextval > 500 or nextval < 0 or onright[nextval] == 0:
                    continue
                c = tex.get(diff, 2) + 1
                if c > res:
                    res = c
                toextend[nextval][diff] = c
            onleft.add(val)
        return res

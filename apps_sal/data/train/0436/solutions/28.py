class Solution:
    def minDays(self, n: int) -> int:
        if n<4:
            return 1 if n==1 else 2
        res, cur = 0, {n}
        def Op(i):
            ans = {i-1}
            if not i%2:
                ans.add(i//2)
            if not i%3:
                ans.add(i//3)
            return ans
        while 0 not in cur:
            cur = {x for i in cur for x in Op(i)}
            res += 1
        return res


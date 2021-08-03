class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        if not p:
            return 0
        l = [[p[i], s[i]] for i in range(len(p))]
        l.sort(reverse=True)
        x = l[0]
        res = 1

        for y in l[1:]:
            t = (target - y[0]) / y[1]
            if t > (target - x[0]) / x[1]:
                res += 1
                x = y
        return res

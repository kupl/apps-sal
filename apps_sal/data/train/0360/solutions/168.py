class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(cap):
            cnt, load = 0, 0
            for x in weights:
                # cap is too small to load even one package
                if x > cap:
                    return False
                if load + x < cap:
                    load += x
                elif load + x == cap:
                    cnt, load = cnt + 1, 0
                else:
                    cnt, load = cnt + 1, x
            return cnt + (load > 0) <= D

        l, r = 1, sum(weights)
        while l < r:
            p = l + (r - l) // 2
            if not check(p):
                l = p + 1
            else:
                r = p
        return l

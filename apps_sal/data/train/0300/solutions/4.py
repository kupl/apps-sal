class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        import math
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def f(x, target, depth):
            if target == 1:
                return 1

            res = target * 2 - 1
            if target < x:
                if x - target < target:
                    res = min(res, 1 + f(x, x - target, depth + 1))
            else:
                y = math.log(target, x)
                y_lower = int(y)
                p = pow(x, y_lower)
                cnt = target // p
                remain = target - cnt * p
                if y > y_lower:
                    res = min(res, y_lower * cnt + f(x, remain, depth + 1))
                    if p * x - target < target:
                        res = min(res, y_lower + 1 + f(x, p * x - target, depth + 1))
                else:
                    res = y_lower - 1
            return res

        return f(x, target, 0)

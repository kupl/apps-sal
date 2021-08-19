class Solution:

    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @lru_cache(None)
        def dp(i, smaller, nonzero, used):
            if i == len(s):
                return nonzero
            ret = 0
            if smaller:
                for dig in range(10):
                    if dig == 0 and (not nonzero):
                        ret += dp(i + 1, True, False, used)
                    else:
                        if 1 << dig & used:
                            continue
                        ret += dp(i + 1, True, True, used | 1 << dig)
            else:
                for dig in range(10):
                    if dig > int(s[i]):
                        break
                    elif dig == int(s[i]):
                        if 1 << dig & used:
                            continue
                        ret += dp(i + 1, False, True, used | 1 << dig)
                    elif dig == 0 and (not nonzero):
                        ret += dp(i + 1, True, False, used)
                    else:
                        if 1 << dig & used:
                            continue
                        ret += dp(i + 1, True, True, used | 1 << dig)
            return ret
        return n - dp(0, False, False, 0)

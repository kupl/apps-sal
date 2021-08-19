class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def foo(dices, need):
            if dices == 0:
                return int(need == 0)
            elif (dices, need) in m:
                return m[dices, need]
            elif need > f * dices:
                m[dices, need] = 0
                return 0
            ret = 0
            for i in range(1, f + 1):
                ret += foo(dices - 1, need - i)
            m[dices, need] = ret
            return ret
        m = {}
        return foo(d, target) % (10 ** 9 + 7)

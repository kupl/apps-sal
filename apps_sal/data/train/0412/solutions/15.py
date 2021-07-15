class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 1000000007
        memo = {}
        def recurseRoll(d, target):
            if d < 0:
                return 0
            if target < 0:
                return 0
            if target == 0 and d == 0:
                return 1
            s = 0
            for i in range(1, f+1):
                if ((d-1,target-i)) in memo:
                    s+=memo[(d-1,target-i)]
                else:
                    s+=recurseRoll(d-1, target-i)
            memo[(d, target)] = s
            return s
        return recurseRoll(d, target) % modulo

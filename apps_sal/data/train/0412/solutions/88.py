class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = [0] * (target + 1)
        memo[0] = 1
        maxV = 10 ** 9 + 7
        for _ in range(d):
            for tv in range(target, -1, -1):
                memo[tv] = 0
                for fv in range(1, f + 1):
                    memo[tv] += memo[tv - fv] if tv - fv >= 0 else 0
                memo[tv] %= maxV
        return memo[-1]
        '\n        memo = {}\n        x = 10**9+7\n        def bt(remD, remT):\n            if remT<0 or remD<0:\n                return 0\n            if (remD, remT) in memo:\n                return memo[(remD, remT)]\n            if remD==0:\n                return 1 if remT==0 else 0\n            temp = 0\n            for i in range(1, f+1):\n                temp += bt(remD-1, remT-i)\n            temp %= x\n            memo[(remD, remT)] = temp\n            return temp\n        \n        return bt(d, target)\n        '
    '\n    (a+b)%c = (a%c+b%c)%c\n    \n    '

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = [0] * (target + 1)
        memo[0] = 1
        maxV = 10**9 + 7
        for _ in range(d):
            for tv in range(target, -1, -1):
                memo[tv] = 0
                for fv in range(1, f + 1):
                    memo[tv] += memo[tv - fv] if tv - fv >= 0 else 0
                memo[tv] %= maxV
        return memo[-1]

        '''
        memo = {}
        x = 10**9+7
        def bt(remD, remT):
            if remT<0 or remD<0:
                return 0
            if (remD, remT) in memo:
                return memo[(remD, remT)]
            if remD==0:
                return 1 if remT==0 else 0
            temp = 0
            for i in range(1, f+1):
                temp += bt(remD-1, remT-i)
            temp %= x
            memo[(remD, remT)] = temp
            return temp
        
        return bt(d, target)
        '''

    '''
    (a+b)%c = (a%c+b%c)%c
    
    '''

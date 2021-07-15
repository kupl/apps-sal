class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        k = 0
        num = []
        t = N
        while t:
            num.append(t%10)
            t = t//10
            k += 1
        num = num[::-1]
        digits = [i for i in range(10)]
        dp = [[0 for _ in range(2)] for _  in range(k+1)]
        def count(dp, dig, state, d1, seen):
            if dig == k:
                return 1
            if dp[dig][state]:
                return dp[dig][state]
            
            seen.add(d1)
            for d in digits:
                if d in seen:
                    continue
                if state == 0:
                    dp[dig][state] += count(dp, dig + 1, state, d, seen)
                elif state == 1:
                    if d > num[dig]:
                        continue
                    if d < num[dig]:
                        dp[dig][state] += count(dp, dig + 1, state^1, d, seen)
                    elif d == num[dig]:
                        dp[dig][state] += count(dp, dig + 1, state, d, seen)
            
            seen.remove(d1)
            return dp[dig][state]
        
        v = 0
        # print(k)
        for d in range(1, 10):
            seen = set()
            if d < num[0]:
                v += count(dp, 1, 0, d, seen)
            elif d == num[0]:
                v += count(dp, 1, 1, d, seen)
        
        
        for i in range(1, k):
            for p in range(1, 10):
                seen = set()
                dp = [[0 for _ in range(2)] for _  in range(k+1)]
                v += count(dp, i + 1, 0, p, seen)
            # print(v)
        # print(dp[3][0])
        return N - v 

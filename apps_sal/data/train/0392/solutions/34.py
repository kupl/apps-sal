class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7

        one = s.count('1')
        if one % 3: return 0
        if one == 0: return ((len(s)-1) * (len(s)-2) // 2) % mod

        k = one // 3
        idx_1, idx_2 = k, k + k
        cnt = a = b = 0
        for d in s:
            if d == '1':
                cnt += 1
            if cnt == idx_1: a += 1
            if cnt == idx_2: b += 1
        
        return (a * b) % mod

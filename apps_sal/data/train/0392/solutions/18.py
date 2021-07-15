class Solution:
    def numWays(self, s: str) -> int:
        k = s.count('1')
        if k % 3:
            return 0
        
        if not '1' in s:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % (10**9 + 7)
        
        k //= 3
        
        l0 = r0 = l1 = r1 = 1 << 60
        cnt = 0
        for i, c in enumerate(s):
            if c == '1':
                cnt += 1
            if cnt == k:
                l0 = min(l0, i)
            if cnt == k + 1:
                l1 = min(l1, i)
            if cnt == 2 * k:
                r0 = min(r0, i)
            if cnt == 2 * k + 1:
                r1 = min(r1, i)
        
        print(l0, l1, r0, r1)
        return (l1 - l0) * (r1 - r0) % (10**9 + 7)

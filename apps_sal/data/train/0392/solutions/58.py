class Solution:
    def numWays(self, s: str) -> int:
        n = s.count('1')
        if n%3!=0:
            return 0
        n = int(n/3)
        if n==0:
            ans = 0
            for i in range(1,len(s)-1):
                ans += len(s)-1-i
            return ans%(10**9 + 7)
        else:
            a = s.split('1')
            return (len(a[n])+1) * (len(a[2*n])+1)%(10**9 + 7)


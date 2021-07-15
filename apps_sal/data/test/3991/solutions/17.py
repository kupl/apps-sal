import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x.sort()
ans = 0
MOD = 10**9+7

for i in range(n-1):
    d = x[i+1]-x[i]
    l = pow(2, i+1, MOD)-1
    r = pow(2, n-i-1, MOD)-1
    ans += d*l*r
    ans %= MOD

print(ans)

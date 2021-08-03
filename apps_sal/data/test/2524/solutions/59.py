N = int(input())
a = list(input().split())
A = [int(a[i])for i in range(N)]
frag = [0 for i in range(60)]
mod = 10 ** 9 + 7
ans = 0

for i in range(60):
    j = 1 << i
    cnt = sum((k & j) >> i for k in A)
    ans += (cnt * (N - cnt)) << i
    ans %= mod

print(ans)

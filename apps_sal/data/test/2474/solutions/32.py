n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
mod = 10 ** 9 + 7
ans = 1
for _ in range(2*n-2):
  ans *= 2
  ans %= mod
cef = [i+2 for i in range(n)]
for i in range(n):
  a[i] *= cef[i]
ans *= sum(a)
ans %= mod
print(ans)

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7
ans = 0
s = sum(a)

for x in a:
  s -= x
  ans += s * x
  ans %= mod
  
ans %= mod
print(ans)

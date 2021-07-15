N = int(input())
A = list(map(int, input().split()))
tmp = 10**10
minus = 0
zeros = 0
ans = 0
for a in A:
  if a > 0:
    ans += a
    tmp = min(tmp, a)
  elif a == 0:
    zeros += 1
  else:
    a = -a
    ans += a
    minus += 1
    tmp = min(tmp, a)
if minus % 2 == 1 and zeros == 0:
  ans -= tmp*2
print(ans)

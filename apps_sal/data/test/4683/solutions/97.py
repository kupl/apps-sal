mod = 10**9+7
n = int(input())
l = list(map(int, input().split()))
ans = []
a = sum(l)
for i in range(len(l)):
  a = a - l[i]
  ans.append(l[i] * a)

print((sum(ans)%mod))




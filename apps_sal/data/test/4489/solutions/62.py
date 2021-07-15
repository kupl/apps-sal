n=int(input())
S=[input() for i in range(n)]
m=int(input())
T=[input() for i in range(m)]
ans=0
for s in set(S):
  ans = max(ans,S.count(s)-T.count(s))
print(ans)

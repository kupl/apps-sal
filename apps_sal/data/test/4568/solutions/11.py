n=int(input())
S=input()
ans=0
for i in range(1,len(S)):
  S1=S[:i]
  S2=S[i:]
  cnt = set()
  for s1 in S1:
    if s1 in S2:
      cnt.add(s1)
  ans = max(ans,len(cnt))
print(ans)

import itertools
n,m,q=map(int,input().split())
abcd=[list(map(int,input().split())) for _ in range(q)]
ans=0
for A in itertools.combinations_with_replacement(range(1,m+1),n):
  score=0
  for a,b,c,d in abcd:
    if A[b-1]-A[a-1]==c:
      score+=d
  ans=max(ans,score)
print(ans)

n,q=map(int,input().split())
ans = [0]*(n)
S = input()
for i in range(n-1):
  tmp = 0
  if S[i] == "A" and S[i+1] == "C":
    tmp = 1
  ans[i+1] = ans[i]+tmp
for i in range(q):
  l,r = map(int,input().split())
  print(ans[r-1]-ans[l-1])

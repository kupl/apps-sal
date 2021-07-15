S=input()
N=len(S)
cnt=N
for i in range(N-1):
  if S[i]!=S[i+1]:
    a=i+1
    b=N-a
    c=max(a,b)
    cnt=min(c,cnt)
print(cnt)

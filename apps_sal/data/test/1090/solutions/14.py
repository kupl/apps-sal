N,K=list(map(int,input().split()))
S=list(input())

c,s=0,S[0]
for n in S[1:]:
  if s==n:
    c+=1
  s=n

print((min(N-1,c+2*K)))


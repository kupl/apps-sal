H,W=map(int,input().split())
L=[[0 for j in range(W)] for i in range(H)]
N=int(input())
R=list()
a=list(map(int,input().split()))
for i in range(N):
  R+=[i+1]*a[i]
for i in range(H):
  if i%2==0:
    s=list(R[i*W:(i+1)*W])
    s=list(map(str,s))
    print(" ".join(s))
  else:
    s=list(R[i*W:(i+1)*W])
    s=list(reversed(s))
    s=list(map(str,s))
    print(" ".join(s))

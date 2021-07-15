#(N-1)*N+K
#N,N,N,N,--NからN-1,N-1,,,N-1はN回
K=int(input())
N=50
S=K//N
T=K%N
L=[N-1+S for i in range(N)]
for i in range(T):
  L[i]+=N+1
for i in range(N):
  L[i]-=T
print(N)
L=list(map(str,L))
print(" ".join(L))

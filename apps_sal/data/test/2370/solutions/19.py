import numpy as np
N = int(input())
A = np.array([list(map(int,input().split())) for _ in range(N)],dtype=np.int64)

INF = 10**9+10
E = np.zeros(((N*(N-1))//2,3),dtype=np.int64)
k = 0
for i in range(N):
    for j in range(i+1,N):
        E[k,0] = A[i][j]
        E[k,1] = i
        E[k,2] = j
        k += 1
E = E[E.argsort(0)[:,0]]
B = np.ones((N,N),dtype=np.int64)*INF
ans = 0
for l,i,j in E:
    l_min = np.min(B[i]+B[j])
    if l > l_min:
        ans = -1
        break
    elif l < l_min:
        ans += l
    B[i][j] = l
    B[j][i] = l
print(ans)

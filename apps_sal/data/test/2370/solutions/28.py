import numpy as np
N=int(input())
A=[np.array(list(map(int,input().split()))) for i in range(N)]
ans=sum([sum(A[i]) for i in range(N)])
ans//=2
for i in range(N):
    A[i][i]=10**10
def main(ans):
    for i in range(N):
        for j in range(i+1,N):
            Min=np.min(A[i]+A[j])
            if Min<A[i][j]:
                return -1
            if Min==A[i][j]:
                ans-=A[i][j]
    return ans
print(main(ans))

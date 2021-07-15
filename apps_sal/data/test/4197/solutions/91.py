N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    A[i]=[A[i],i]
A.sort()
for i in range(N):
    print(A[i][1]+1,end=' ')
print()


n=int(input())

A=list(map(int,input().split()))

A.sort()

print(A[-1],end=" ")
for i in range(1,n-1):
    print(A[i],end=" ")
print(A[0])


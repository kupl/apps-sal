n=int(input())
A = list(map(int, input().split()))
B=A[:]
max=0
for i in range(n):
    for k in range(n):
        for z in range(i,k+1):
            if A[z]==1:
                A[z]=0
            else:
                A[z]=1
            if A.count(1)>max:
                max=A.count(1)
        A=B[:]
print(max)

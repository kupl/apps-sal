n = int(input())
A = list(map(int, input().split()))
a = sum(A)//n
for i in range(n):
    e=a-A[0]
    for j in range(1, 2*n):
        if A[j]==e:
            print(A[0], A[j])
            del A[j]
            del A[0]
            break

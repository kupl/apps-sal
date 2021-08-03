n, m = list(map(int, input().split()))
A = input().split()
B = input().split()

A.sort()
B.sort()

for i in A:
    if i in B:
        print(i)
        return


if(A[0] < B[0]):
    print(A[0] + B[0])
else:
    print(B[0] + A[0])

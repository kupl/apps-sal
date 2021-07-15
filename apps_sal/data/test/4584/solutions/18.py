N = int(input())
A = [0]*(N)
for i in input().split():
    A[int(i)-1] = A[int(i)-1]+1
for i in A:
    print(i)


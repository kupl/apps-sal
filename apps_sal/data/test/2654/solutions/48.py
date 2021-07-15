N = int(input())
A = [0]*N
B = [0]*N

for i in range(N):
    A[i], B[i] = map(int, input().split())

A = sorted(A)
B = sorted(B)

if N % 2 == 1:
    print(B[(N+1)//2-1] - A[(N+1)//2-1] + 1)
else:
    b = B[N//2-1] + B[N//2]
    a = A[N//2-1] + A[N//2]
    print(b-a+1)

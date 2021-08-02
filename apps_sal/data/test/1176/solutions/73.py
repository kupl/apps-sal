N = int(input())
A = [int(_) for _ in input().split()]

cnt = 0
for i in range(N):
    if A[i] < 0:
        cnt += 1
        A[i] *= -1

if cnt % 2 == 0:
    print((sum(A)))
else:
    print((sum(A) - min(A) * 2))

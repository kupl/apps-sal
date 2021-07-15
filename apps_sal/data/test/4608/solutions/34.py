N = int(input())
A = [int(input()) for _ in range(N)]

A = [0] + A
i = 1
k = 1
while k <= N:
    if A[i] == 2:
        print(k)
        return
    i = A[i]
    k += 1
print((-1))


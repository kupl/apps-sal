N = int(input())
A = [int(x) for x in input().split()]
M = 0
for i in range(N, 0, -1):
    t = 0
    for j in range(i, N + 1, i):
        t += A[j - 1]
    if t % 2 != A[i - 1]:
        A[i - 1] = (A[i - 1] + 1) % 2
    if A[i - 1]:
        M += 1
print(M)
if M > 0:
    for i in range(N):
        if A[i]:
            print(i + 1, '', end='')
    print()

N = int(input())
A = sorted(list(map(int, input().split())))[::-1]
for n in range(N - 1):
    if A[n] == A[n + 1]:
        A[n + 1] = 0
    else:
        A[n] = 0
A = sorted(A)[::-1]
print(A[0] * A[1])

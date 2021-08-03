N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N):
    realnum = int(i + 1)

    if A[i] == realnum:
        if A[i] == N:
            A[i - 1], A[i] = A[i], A[i - 1]
        else:
            A[i], A[i + 1] = A[i + 1], A[i]

        count = count + 1

print(count)

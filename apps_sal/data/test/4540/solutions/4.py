N = int(input())
A = list(map(int, input().split()))
j = abs(A[0]) + abs(A[N - 1])
for i in range(N - 1):
    j += abs(A[i] - A[i + 1])
for i in range(N):
    if i == 0:
        ans = j - abs(A[0]) - abs(A[0] - A[1]) + abs(A[1])
    elif i == N - 1:
        ans = j - abs(A[N - 2] - A[N - 1]) - abs(A[N - 1]) + abs(A[N - 2])
    else:
        ans = j - abs(A[i] - A[i - 1]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1])
    print(ans)

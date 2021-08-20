(N, X) = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    temp = 0
    if A[i] + A[i + 1] <= X:
        continue
    else:
        temp = A[i] + A[i + 1] - X
        if A[i + 1] < temp:
            A[i + 1] = 0
            cnt += A[i + 1]
            temp -= A[i + 1]
        else:
            A[i + 1] -= temp
            cnt += temp
            temp -= A[i + 1]
        if A[i] + A[i + 1] > X:
            A[i] -= temp
            cnt += temp
print(cnt)

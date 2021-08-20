N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if A[i] == i + 1:
        (A[i], A[i + 1]) = (A[i + 1], A[i])
        cnt += 1
        i += 1
if A[N - 1] == N:
    cnt += 1
print(cnt)

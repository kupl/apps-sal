N = int(input())
(D, X) = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    day = 1
    while day <= D:
        cnt += 1
        day += A[i]
print(cnt + X)

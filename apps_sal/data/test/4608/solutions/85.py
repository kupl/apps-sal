n = int(input())
A = [int(input()) for _ in range(n)]

now = 0
cnt = 0
while A[now] != 2 and cnt <= n:
    now = A[now] - 1
    cnt += 1

if A[now] == 2:
    print((cnt + 1))
else:
    print((-1))

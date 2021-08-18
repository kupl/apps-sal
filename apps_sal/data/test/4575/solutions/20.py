N = int(input())
D, X = list(map(int, input().split()))
A = [int(input()) for _ in range(N)]

eaten = 0
for i in range(N):
    day = 0
    cnt = 0
    while True:
        day = A[i] * cnt + 1
        if day <= D:
            eaten += 1
            cnt += 1
        else:
            break
print((eaten + X))

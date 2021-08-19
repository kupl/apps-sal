N = int(input())
ops = 0
if N % 2 == 0 or N % 5 == 0:
    ops = 1
else:
    if N % 7 == 0:
        L = 9 * N // 7
    else:
        L = 9 * N
    ch = 10 % L
    for i in range(1, N + 1):
        if ch == 1:
            ans = i
            break
        ch = 10 * ch % L
        if i == N + 1:
            ops = 1
if ops:
    print(-1)
else:
    print(ans)

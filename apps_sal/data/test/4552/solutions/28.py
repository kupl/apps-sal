N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]
ans = -10 ** 9
for i in range(1, 2 ** 10):
    s = i
    b = [0] * 10
    for j in range(10):
        if s >= 2 ** (10 - j - 1):
            s -= 2 ** (10 - j - 1)
            b[j] = 1
    a = 0
    for j in range(N):
        c = 0
        for k in range(10):
            if b[k] == 1 and F[j][k] == 1:
                c += 1
        a += P[j][c]
    ans = max(ans, a)
print(ans)

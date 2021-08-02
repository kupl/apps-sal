n = int(input())
F = [0] * n
P = [0] * n
for i in range(n):
    F[i] = list(map(int, input().split()))
for i in range(n):
    P[i] = list(map(int, input().split()))

ans = -float("Inf")
for i in range(1, 2**10):
    L = []
    b = 0
    for j in range(10):
        if (i >> j) & 1:
            L.append(j)
    for j in range(n):
        c = 0
        for x in L:
            if F[j][x] == 1:
                c += 1
        b += P[j][c]

    ans = max(ans, b)


print(ans)

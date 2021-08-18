import sys

ans = sys.maxsize
H, W, K = list(map(int, input().split()))
s = [input() for _ in range(H)]

for h in range(1 << (H - 1)):
    g = 0
    ids = [-1 for _ in range(H)]
    for i in range(H):
        ids[i] = g
        if (h >> i) & 1:
            g += 1

    g += 1
    num = g - 1

    if num >= ans:
        continue

    c = [[0] * W for _ in range(g)]
    for i in range(H):
        for j in range(W):
            c[ids[i]][j] = c[ids[i]][j] + (s[i][j] == '1')

    now = [0 for _ in range(g)]

    def add(j):
        for i in range(g):
            now[i] += c[i][j]

        for i in range(g):
            if now[i] > K:
                return False

        return True

    for j in range(W):
        if not add(j):
            num += 1
            if num >= ans:
                continue
            now = [0 for _ in range(g)]
            if not add(j):
                num = sys.maxsize
                break

    ans = min(ans, num)

print(ans)

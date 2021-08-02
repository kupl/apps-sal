H, W, K = map(int, input().split())
P = []
for i in range(H):
    s = input()
    a = []
    for j in range(W):
        a.append(s[j])
    P.append(a)

ans = 0
for markR in range(2**H):
    for markC in range(2**W):
        black = 0
        for i in range(H):
            for j in range(W):
                if (markR >> i) & 1 == 0 and (markC >> j) & 1 == 0 and P[i][j] == '#':
                    black += 1
        if black == K:
            ans += 1

print(ans)

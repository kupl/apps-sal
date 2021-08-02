import itertools
H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

ans = 0
for i in range(H + 1):
    for j in range(W + 1):
        for row in itertools.combinations([x for x in range(H)], i):
            for column in itertools.combinations([x for x in range(W)], j):
                tmp = 0
                for tr in range(H):
                    for tc in range(W):
                        if tr in row:
                            continue
                        if tc in column:
                            continue
                        if c[tr][tc] == '#':
                            tmp += 1
                if tmp == K:
                    ans += 1
print(ans)

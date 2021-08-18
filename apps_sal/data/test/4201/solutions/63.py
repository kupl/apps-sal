H, W, K = map(int, input().split())
c = [["." for _ in range(W)] for _ in range(H)]

for h in range(H):
    c[h] = input()

ans = 0
for i in range(2 ** H):
    for k in range(2 ** W):
        count = 0
        for h in range(H):
            for w in range(W):
                if (i >> h) & 1 and (k >> w) & 1:
                    if c[h][w] == "
                    count += 1

        if count == K:
            ans += 1
print(ans)

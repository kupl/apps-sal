h, w, k = map(int, input().split())
ccc = [input() for _ in range(h)]
ans = 0
for bit_h in range(2 ** h):
    for bit_w in range(2 ** w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if (bit_h >> i) & 1 == 0 and (bit_w >> j) & 1 == 0:
                    if ccc[i][j] == '#':
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)

h, w, k = map(int, input().split())
ccc = [input() for _ in range(h)]
ans = 0
for bit_h in range(2 ** h):
    for bit_w in range(2 ** w):
        cnt = 0
        for hi in range(h):
            for wi in range(w):
                if (bit_h >> hi) & 1 == 0 and (bit_w >> wi) & 1 == 0:
                    if ccc[hi][wi] == '#':
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)

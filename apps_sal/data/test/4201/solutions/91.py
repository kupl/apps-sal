(h, w, k) = map(int, input().split())
c = [input() for x in range(h)]
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        count = 0
        for m in range(h):
            for n in range(w):
                if i >> m & 1 == 0 and j >> n & 1 == 0 and (c[m][n] == '#'):
                    count += 1
        if count == k:
            ans += 1
print(ans)

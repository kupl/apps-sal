h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
for row in range(2**h):
    for col in range(2**w):
        c = 0
        for i in range(h):
            for j in range(w):
                if (row >> i) & 1 == 0 and (col >> j) & 1 == 0:
                    if s[i][j] == '#':
                        c += 1
        if c == k:
            ans += 1
print(ans)

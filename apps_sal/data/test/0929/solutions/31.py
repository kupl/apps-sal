h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(h)]

ans = []

c = 0
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if c == 0 and a[i][j] % 2 == 1:
                c = 1
            if c == 2:
                c = 0
            if c == 1 and j < w - 1:
                ans.append([str(i + 1), str(j + 1), str(i + 1), str(j + 2)])
                if a[i][j + 1] % 2 == 1:
                    c = 2
            elif c == 1 and j == w - 1 and i + 1 <= h - 1:
                ans.append([str(i + 1), str(j + 1), str(i + 2), str(j + 1)])
                if a[i + 1][j] % 2 == 1:
                    c = 2
    if i % 2 == 1:
        for j in range(w):
            if c == 0 and a[i][w - 1 - j] % 2 == 1:
                c = 1
            if c == 2:
                c = 0
            if c == 1 and j < w - 1:
                ans.append([str(i + 1), str(w - j), str(i + 1), str(w - j - 1)])
                if a[i][w - j - 2] % 2 == 1:
                    c = 2
            elif c == 1 and j == w - 1 and i + 1 <= h - 1:
                ans.append([str(i + 1), str(w - j), str(i + 2), str(w - j)])
                if a[i + 1][w - 1 - j] % 2 == 1:
                    c = 2
print((len(ans)))
for i in ans:
    print((' '.join(i)))

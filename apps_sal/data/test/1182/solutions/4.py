r, c, n, k = map(int, input().split())
s = [[0] * c for i in range(r)]
for i in range(n):
    x, y = map(int, input().split())
    s[x - 1][y - 1] = 1
res = 0
for br in range(r):
    for bc in range(c):
        for er in range(br, r):
            for ec in range(bc, c):
                counter = 0
                for i in range(br, er + 1):
                    for j in range(bc, ec + 1):
                        if s[i][j] == 1:
                            counter += 1
                if counter >= k:
                    res += 1

print(res)

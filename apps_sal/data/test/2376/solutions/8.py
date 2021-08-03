n, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[] for _ in range(4)]
for i, j in a:
    b[i - a[0][0]].append(j)
for i in range(4):
    b[i].sort()
    b[i].reverse()
for i in range(4):
    for j in range(1, len(b[i])):
        b[i][j] += b[i][j - 1]
    b[i].reverse()
    b[i].append(0)
    b[i].reverse()
# print(b)
ans = 0
for i in range(len(b[0])):
    for j in range(len(b[1])):
        for k in range(len(b[2])):
            for l in range(len(b[3])):
                # print(i,j,k,l)
                if a[0][0] * i + (a[0][0] + 1) * j + (a[0][0] + 2) * k + (a[0][0] + 3) * l <= w:
                    # print(i,j,k,l)
                    ans = max(ans, b[0][i] + b[1][j] + b[2][k] + b[3][l])
print(ans)

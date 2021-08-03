from collections import defaultdict as dd
n, s = (i for i in input().split())
n, ans = int(n), 0
x, d = [[0] * 2 for i in range(n + 1)], dd(int)
for i in range(n):
    for j in range(2):
        x[i + 1][j] = x[i][j]
    if s[i] == "A":
        x[i + 1][0] = x[i][0] + 1
    elif s[i] == "T":
        x[i + 1][0] = x[i][0] - 1
    elif s[i] == "C":
        x[i + 1][1] = x[i][1] + 1
    else:
        x[i + 1][1] = x[i][1] - 1
for i, j in x:
    z = str(i) + " " + str(j)
    d[z] += 1
for i in d.values():
    ans += i * (i - 1) // 2
print(ans)

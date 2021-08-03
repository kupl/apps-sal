from sys import stdin, stdout

INF = float('inf')
n, m = map(int, stdin.readline().split())
fst = [[INF, INF, INF] for i in range(n)]

for i in range(n):
    s = list(stdin.readline().strip())
    for j in range(m):
        if '9' >= s[j] >= '0' or '9' >= s[-j] >= '0':
            fst[i][0] = min(fst[i][0], j)

        if 'z' >= s[j] >= 'a' or 'z' >= s[-j] >= 'a':
            fst[i][1] = min(fst[i][1], j)

        if s[j] in '#*&' or s[-j] in '#*&':
            fst[i][2] = min(fst[i][2], j)


ans = INF
for i in range(n):
    for j in range(n):
        for z in range(n):
            if i == j or i == z or j == z:
                continue

            ans = min(fst[i][0] + fst[j][1] + fst[z][2], ans)

stdout.write(str(ans))

n, k = list(map(int, input().split()))
m = [list(input()) for _ in range(n)]
p = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        s = True
        if i + k - 1 < n:
            for l in range(k):
                if m[i + l][j] != '.':
                    s = False
                    break
            if s:
                for l in range(k):
                    p[i + l][j] += 1

        s = True
        if j + k - 1 < n:
            for l in range(k):
                if m[i][j + l] != '.':
                    s = False
                    break
            if s:
                for l in range(k):
                    p[i][j + l] += 1

mx = -1
for i in range(n):
    for j in range(n):
        if p[i][j] > mx:
            ans = (i + 1, j + 1)
            mx = p[i][j]

print(*ans)

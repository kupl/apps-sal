(r, c, n, k) = map(int, input().split())
A = [[0] * c for i in range(r)]
for i in range(n):
    (a, b) = map(int, input().split())
    A[a - 1][b - 1] = 1
f = 0
g = 0
ans = 0
for i in range(r):
    for j in range(c):
        for i2 in range(r - i):
            for j2 in range(c - j):
                cnt = 0
                for i3 in range(i, i + i2 + 1):
                    for j3 in range(j, j + j2 + 1):
                        cnt += int(A[i3][j3] == 1)
                if cnt >= k:
                    ans += 1
print(ans)

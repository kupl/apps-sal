import sys
n = int(input())
F = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
P = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = -pow(10, 9) - 7
for i in range(1, pow(2, 10)):
    b = bin(i)[2:].zfill(10)
    t = 0
    for j in range(n):
        c = 0
        for k in range(10):
            if int(b[k]) and F[j][k]:
                c += 1
        t += P[j][c]
    ans = max(ans, t)
print(ans)

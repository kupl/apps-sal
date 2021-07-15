import sys
input = sys.stdin.readline

n,k = map(int, input().split())
grid = [[0]*k for i in range(k)]
black = 0
for i in range(n):
    a,b,c =input().split()
    a,b = int(a), int(b)
    f = a//k + b//k
    a %= k
    b %= k
    if (c == "W" and f%2==0) or (c == "B" and f%2==1):
        grid[a][b] += 1
    else:
        grid[a][b] -= 1
        black += 1

s = [[0]*(k+1) for i in range(k+1)]
for i in range(k):
    for j in range(k):
        s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + grid[i][j]

ans = 0
for i in range(k):
    for j in range(k):
        a = s[k][k] - s[i][k] - s[k][j] + 2*s[i][j] + black
        ans = max(ans, max(a, n-a))
print(ans)

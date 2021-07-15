import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n//2):
        for j in range(m//2):
            tmp = [a[i][j], a[i][m-j-1], a[n-i-1][j], a[n-i-1][m-j-1]]
            tmp.sort()
            ans += tmp[3]+tmp[2]-tmp[1]-tmp[0]
    if n%2:
        for j in range(m//2):
            ans += abs(a[n//2][j]-a[n//2][m-j-1])
    if m%2:
        for i in range(n//2):
            ans += abs(a[i][m//2]-a[n-i-1][m//2])
    print(ans)

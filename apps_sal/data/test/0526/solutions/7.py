import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
ans = [1]*n
res = 0
for i in range(n):
    res ^= a[i][0]
if res != 0:
    print("TAK")
    print(*ans)
    return

for i in range(n):
    res ^=a[i][0]
    for j in range(m):
        res ^=a[i][j]
        if res != 0:
            ans[i] = j+1
            print("TAK")
            print(*ans)
            return
        res ^=a[i][j]
    res ^= a[i][0]
print("NIE")

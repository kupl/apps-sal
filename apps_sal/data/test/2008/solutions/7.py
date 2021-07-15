import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    a[i].append(a[i][0]-a[i][1])
a.sort(key = lambda x:-x[2])
ans = 0
for i in range(n):
    ans += a[i][0]*i + a[i][1]*(n-i-1)
print(ans)

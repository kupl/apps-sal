import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(key=lambda x: -x)
go = sum(a)
ans = (go + min(n * k, m)) / n
for i in range(n - 1):
    ke = a.pop()
    m -= 1
    go -= ke
    if m < 0:
        break
    ans = max(ans, (go + min(((n - 1 - i) * k), m)) / (n - 1 - i))
print(ans)

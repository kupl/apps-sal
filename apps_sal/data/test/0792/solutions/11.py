#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7
sys.setrecursionlimit(1000000)

n, d = map(int, input().split())
a = list(map(int, input().split()))
p = [0 for i in range(n)]
for i in range(n):
    p[i] = p[i-1]+a[i]
mx = [-1 for i in range(n)]
mx[-1] = p[-1]
for i in range(n-2, -1, -1):
    mx[i] = max(mx[i+1], p[i])
c = 0
ans = 0
for i in range(n):
    p[i] += c
    if p[i] > d:
        print(-1)
        return
    if a[i] != 0 or p[i] >= 0: continue

    av = d-(mx[i]+c)
    if -p[i] > av:
        print(-1)
        return
    ans += 1
    c = d-mx[i]
print(ans)

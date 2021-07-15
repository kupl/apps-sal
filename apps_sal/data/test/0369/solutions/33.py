import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,m = na()
s = list(ns())
s = s[::-1] #n+1

ans = []
i = 0
while True:
    j = i+m if i+m < n else n
    for k in reversed(range(i+1,j+1)):
        if s[k] == '0':
            ans.append(k-i)
            i = k
            break
    else:
        print(-1)
        return
    if i == n:
        break

print(*ans[::-1],sep=' ')

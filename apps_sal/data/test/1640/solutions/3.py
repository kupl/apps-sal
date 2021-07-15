def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())
from collections import defaultdict

n = ii()
a = li()

def calc(a):
    d = defaultdict(int)
    s = 0
    for i in range(n):
        x = a[i]
        s += (i - d[x] - d[x-1] - d[x+1]) * x
        d[x] += 1
    return s

ans = calc(a) - calc(a[::-1])
print(ans)


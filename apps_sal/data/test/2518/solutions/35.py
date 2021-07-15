import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,a,b = list(map(int, input().split()))
h = list(int(input()) for i in range(n))

diff = a-b

hmax = max(h)

saiaku = -(-hmax//b)

def isok(ans):
    count = 0
    for i in range(n):
        count += max(-(-(h[i]-b*ans)//diff),0)
    if count > ans:
        return False
    return True

ok = saiaku
ng = -1 # -1にしとけば答えが0の時も普通に扱えるな

while ok - ng > 1:
    m = (ok+ng)//2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)


import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


k = II()
x, y = MI()

# Kが偶数で、ゴールまでのマンハッタン距離が奇数だと不可能
if k % 2 == 0 and (x + y) % 2:
    print(-1)
    return

# x>=0,y>=0,x<=yに修正して解き、最後に復元
cx = -1 if x < 0 else 1
cy = -1 if y < 0 else 1
x, y = abs(x), abs(y)
swap = False
if x > y:
    swap = True
    x, y = y, x

ans = []
if (x + y) % 2 and x + y < k:
    ans.append((x, y))
    y += k
l = (x + y + k - 1) // k * k
if (l - x - y) % 2:
    l += k
d = (l - x - y) // 2
if d > 0 and d + y < k:
    d += k // 2

if d:
    ans.append((x, y))
    x += d
    y -= k - d

while y - k >= 0:
    ans.append((x, y))
    y -= k

if y:
    ans.append((x, y))
    x -= k - y
    y = 0

while x > 0:
    ans.append((x, y))
    x -= k

print(len(ans))
for x, y in ans[::-1]:
    if swap:
        x, y = y, x
    print(cx * x, cy * y)

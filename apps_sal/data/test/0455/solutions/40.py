import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def parity():
    res = sum(xy[0]) % 2
    for x, y in xy:
        if (x + y) % 2 != res: return -1
    return res


n = II()
xy = LLI(n)

p = parity()
if p == -1:
    print(-1)
    return

dd = [1]
if p == 0: dd.append(1)
lim = 10**12
while len(dd) < 40 and dd[-1] * 2 <= lim:
    dd.append(dd[-1] * 2)
print(40)
print(*dd)

for x, y in xy:
    ans = ""
    for d in dd[::-1]:
        if abs(x) > abs(y):
            if x > 0:
                x -= d
                ans += "R"
            else:
                x += d
                ans += "L"
        else:
            if y > 0:
                y -= d
                ans += "U"
            else:
                y += d
                ans += "D"
    print(ans[::-1])

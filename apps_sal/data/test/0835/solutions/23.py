recipe = input()
rb = rs = rc = 0
nb, ns, nc = list(map(int, input().split()))
pb, ps, pc = list(map(int, input().split()))
r = int(input())

for ch in recipe:
    if ch == "B":
        rb += 1
    elif ch == "S":
        rs += 1
    else:
        rc += 1

a = 0
b = 10 ** 12 + 1000


def doable(n):
    return r >= pb * max(0, rb * n - nb) + ps * max(0, rs * n - ns) + pc * max(0, rc * n - nc)


res = 0
while a <= b:
    m = (a + b) // 2
    if doable(m):
        res = m
        a = m + 1
    else:
        b = m - 1

print(res)

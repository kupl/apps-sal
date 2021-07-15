from time import time as tm

b, a = list(map(int, input().split()))
d, c = list(map(int, input().split()))
cur = ma = mb = 0

stm = tm()

while tm() - stm < 0.9:
    isa = (a + b * ma) == cur
    isb = (c + d * mb) == cur
    if isa:
        ma += 1
    if isb:
        mb += 1
    if isa and isb:
        print(cur)
        break
    cur += 1
else:
    print(-1)


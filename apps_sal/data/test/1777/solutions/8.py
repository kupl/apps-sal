from collections import Counter
N = int(input())
S = [input() for i in range(N)]
c1 = Counter()
c2 = Counter()
zeros = 0
for s in S:
    op = nop = 0
    for c in s:
        if c == '(':
            op += 1
        elif op == 0:
            nop += 1
        else:
            op -= 1
    if op and nop:
        continue
    if op:
        c1[op] += 1
    elif nop:
        c2[nop] += 1
    else:
        zeros += 1
print(sum((c1 & c2).values()) + zeros // 2)

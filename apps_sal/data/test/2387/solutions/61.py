# F - Bracket Sequencing

from itertools import chain

n = int(input())
ss = [input() for i in range(n)]

def parse(s):
    "バランスしていない閉じ括弧数, 開き括弧数"
    cl, op = 0, 0
    for c in s:
        if c == '(':
            op += 1
        elif op > 0:
            op -= 1
        else:
            cl += 1
    return (cl, op)

open  = []  # 開き括弧のみ
close = []  # 閉じ括弧のみ
inc   = []  # 開き括弧が多い
dec   = []  # 閉じ括弧が多い
for s in ss:
    cl, op = parse(s)
    if cl == 0:
        open.append((cl, op))
    elif cl < op:
        inc.append((cl, op))
    elif op == 0:
        close.append((cl, op))
    else:
        dec.append((cl, op))
peak = 0
inc.sort()
dec.sort(reverse=True)
for cl, op in chain(open, inc, dec, close):
    if peak < cl:
        print('No')
        return
    peak += op - cl
print(('Yes' if peak == 0 else 'No'))


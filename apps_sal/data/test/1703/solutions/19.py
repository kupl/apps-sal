maxn = 4 * (10**5)
n = int(input().strip())
openers = [0] * maxn
closers = [0] * maxn


def check_opener(seq):
    op_br = 0
    for c in seq:
        if c == '(':
            op_br += 1
        else:
            op_br -= 1
        if op_br < 0:
            return -1
    return op_br


def check_closer(seq):
    op_br = 0
    for c in seq[::-1]:
        if c == ')':
            op_br += 1
        else:
            op_br -= 1
        if op_br < 0:
            return -1
    return op_br


for _ in range(n):

    seq = input().strip()

    r = check_opener(seq)
    if r >= 0:
        openers[r] += 1

    r = check_closer(seq)
    if r >= 0:
        closers[r] += 1

res = 0
for i in range(maxn):
    res += openers[i] * closers[i]

print(res)

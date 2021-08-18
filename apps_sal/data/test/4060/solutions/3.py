_ = input()
s = list(input())


def regular(s):
    k = 0
    for c in s:
        if c == '(':
            k += 1
        elif c == ')':
            k -= 1
        if k < 0:
            return False
    return k == 0


def regular_sums(s):
    k = 0
    ks = []
    for c in s:
        if c == '(':
            k += 1
        elif c == ')':
            k -= 1
        ks.append(k)
    return ks


sums = regular_sums(s)

if sums[-1] == 2:
    ia = 0
    while ia < len(sums) and sums[ia] >= 0:
        ia += 1

    ib = len(s) - 1
    while ib >= 0 and sums[ib] >= 2:
        ib -= 1

    k = 0
    for i in range(max(ib + 1, 0), min(ia + 1, len(s))):
        if s[i] == '(':
            k += 1
    print(k)
elif sums[-1] == -2:
    ia = 0
    while ia < len(sums) and sums[ia] >= 0:
        ia += 1

    ib = len(s) - 1
    while ib >= 0 and sums[ib] >= -2:
        ib -= 1

    k = 0
    for i in range(max(ib + 1, 0), min(ia + 1, len(s))):
        if s[i] == ')':
            k += 1
    print(k)
else:
    print(0)

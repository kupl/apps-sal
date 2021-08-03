n = int(input())
lrs = []

alr = input().split()
al = int(alr[0])
ar = int(alr[1])
at = ar - al

for i in range(n - 1):
    lr = input().split()
    l = (int(lr[0]), 'l')
    r = (int(lr[1]), 'r')
    lrs.append(l)
    lrs.append(r)

slrs = sorted(lrs, key=lambda x: x[0])

c = 0
lt = 101

for i in range(2 * (n - 1)):
    cur = slrs[i]
    if cur[1] == 'l':
        c += 1
        if c == 1:
            lt = cur[0]
    else:
        c -= 1
        if c == 0:
            if al <= cur[0] and cur[0] <= ar:
                if lt >= al:
                    at -= (cur[0] - lt)
                elif lt < al:
                    at -= (cur[0] - al)
            elif ar < cur[0]:
                if lt <= al:
                    at = 0
                elif al < lt and lt < ar:
                    at -= (ar - lt)
            if at <= 0:
                break
            lt = 101

print(at)

n, k = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]

f = 0
while f < n and w[f] >= 0:
    f += 1

if f == n:
    print(0)
    return

b = n - 1
while b >= 0 and w[b] >= 0:
    b -= 1

# if n == b - f + 1:
#     print(1)
#     return

if f == b:
    if k == 0:
        print(-1)
        return

    if f+1 == n:
        print(1)
        return
    else:
        if (k - 1) >= (n - (b + 1)):
            print(1)
            return
        else:
            print(2)
            return

inv = []
ps = 0
ns = 0
for i in range(f, b):
    if w[i] >= 0:
        ps += 1
        if w[i+1] < 0:
            inv.append(ps)
    elif w[i] < 0:
        ns += 1
        if w[i+1] >= 0:
            ps = 0
ns += 1
spare = k - ns

if spare < 0:
    print(-1)
    return

if not inv:
    if w[n-1] < 0:
        print(1)
        return
    else:
        if spare >= (n - (b + 1)):
            print(1)
            return
        else:
            print(2)
            return

invs = sorted(inv)

if spare < invs[0]:
    ch = (len(invs) + 1) * 2
    remainder = spare
else:
    use, invsn = invs[0], -1
    for i in range(1, len(invs)):
        use += invs[i]
        if spare < use:
            use -= invs[i]
            invsn = i
            break

    if invsn == -1:
        invsn = len(invs)

    ch = (len(invs) - invsn + 1) * 2
    remainder = spare - use

if remainder >= (n - (b + 1)):
    ch -= 1

print(ch)



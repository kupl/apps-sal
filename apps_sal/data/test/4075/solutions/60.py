(n, m) = map(int, input().split())
ks = []
ss = []
for _ in range(m):
    row = list(map(lambda x: int(x) - 1, input().split()))
    ks.append(row[0] + 1)
    ss.append(row[1:])
ps = list(map(int, input().split()))


def is_bulb_on(bits, i):
    cnt = 0
    for s in ss[i]:
        if bits[s]:
            cnt += 1
    return cnt % 2 == ps[i]


def are_all_bulb_on(bits):
    good = True
    i = 0
    while good and i < m:
        good &= is_bulb_on(bits, i)
        i += 1
    return good


def rec(bits, i):
    if i == n:
        return 1 if are_all_bulb_on(bits) else 0
    cnt = 0
    cnt += rec(bits, i + 1)
    bits[i] = 1
    cnt += rec(bits, i + 1)
    bits[i] = 0
    return cnt


bits = [0] * n
print(rec(bits, 0))

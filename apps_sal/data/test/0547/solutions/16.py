def getin():
    xin = input()
    while xin.strip() == "":
        xin = input()
    return xin


def gi():
    return [int(x) for x in getin().split()]


def count(n, k):
    return int(n / k) * k + int((n - 1) / k) * 5 + n % k


n, k = gi()
m = -1

c = [0] * 109
p = []

for i in range(n):
    s = input()
    c[len(s)] += 1
    if len(s) > m:
        m = len(s)
    p.append(s)

ac = input()

if ac not in p:
    print(count(n, k), count(n, k))
else:
    i = 1
    mi = 0
    while i < len(ac):
        mi += c[i]
        i += 1

    print(count(mi + 1, k), count(mi + c[len(ac)], k))

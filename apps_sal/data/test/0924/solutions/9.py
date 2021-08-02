l1, r1, t1 = list(map(int, input().split()))
l2, r2, t2 = list(map(int, input().split()))
# a=list(map(int,input().split()))


def gcd(a, b):
    if a > b: a, b = b, a
    while a > 0:
        b = b % a
        a, b = b, a
    return b


d = gcd(t1, t2)


def answer(x1, d1, x2, d2):
    if x1 > x2:
        x1, x2, d1, d2 = x2, x1, d2, d1
    d1 = d1 - (x2 - x1)
    if d1 < 0: d1 = 0
    return min(d1, d2)


d1 = r1 - l1 + 1
d2 = r2 - l2 + 1

l1 = l1 % d
l2 = l2 % d

if l1 > l2:
    l1, l2, d1, d2 = l2, l1, d2, d1

ans1 = answer(l1, d1, l2, d2)
ans2 = answer(l1 + d, d1, l2, d2)

print(max(ans1, ans2))

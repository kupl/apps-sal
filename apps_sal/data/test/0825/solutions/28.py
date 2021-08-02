import bisect
n = int(input())
if n == 1:
    print(0)
    return


def factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def ra(a):
    ll, l = [], 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            l += 1
        else:
            ll.append(l)
            l = 1
    ll.append(l)
    return ll


l = ra(factorize(n))
c = [1]
for i in range(2, 10**4):
    c.append(i + c[-1])
ans = 0
for i in l:
    ans += bisect.bisect_left(c, i)
    if i in set(c):
        ans += 1
print(ans)

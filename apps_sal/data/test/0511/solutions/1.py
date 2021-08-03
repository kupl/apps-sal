def sqrt(n):
    return n**.5


def pfs(n):
    A = []
    while n % 2 == 0:
        A += [2]
        n //= 2
    return A + pfs_dummy(n, 3)


def pfs_dummy(n, start):
    if n == 1:
        return []
    A = []
    for k in range(start, int(sqrt(n) + 1), 2):
        if n % k == 0:
            while n % k == 0:
                A.append(k)
                n //= k
            return A + pfs_dummy(n, k + 2)
    if len(A) == 0:
        return [n]


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b % a, a)


s = input()
x = int(s.split()[0])
y = int(s.split()[1])

d = gcd(x, y)
x //= d
y //= d

arr = pfs(x)
ans = 0

while y > 0:
    if x == 1:
        ans += y
        y = 0

    else:
        maxcand = -1
        for p in set(arr):
            maxcand = max(maxcand, y - (y % p))
        ans += (y - maxcand)
        y = maxcand
        e = gcd(x, y)
        x //= e
        y //= e
        arr1 = pfs(e)
        for pf in arr1:
            arr.remove(pf)

print(ans)

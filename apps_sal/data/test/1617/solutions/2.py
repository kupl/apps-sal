def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base ** exponent
    return a


def fact(n):
    fct = factorize(n)
    res = []
    for div in divisorize(fct):
        res.append(num(div))
    return res


def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


def f(n, k):
    return n * (n - k + 2) // k // 2


n = read()
k_list = fact(n)

ans = []
for k in k_list:
    ans.append(f(n, k))

ans.sort()

print(" ".join(list(map(str, ans))))

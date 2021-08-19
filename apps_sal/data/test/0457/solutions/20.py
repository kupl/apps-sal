"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10 ** 7)


def iin():
    return int(stdin.readline())


def lin():
    return list(map(int, stdin.readline().split()))


(x, n) = lin()
md = 10 ** 9 + 7


def factors(a):
    fact = []
    if a % 2 == 0:
        while a % 2 == 0:
            a //= 2
        fact.append(2)
    i = 3
    while i * i <= a:
        if a % i == 0:
            while a % i == 0:
                a //= i
            fact.append(i)
        i += 2
    if a > 1:
        fact.append(a)
    return fact


fact = factors(x)
ans = 1
for f in fact:
    x = f
    ch = 0
    while x <= n:
        ch += n // x
        x *= f
    ans = ans * pow(f, ch, md)
    ans %= md
ans = ans % md
print(ans)

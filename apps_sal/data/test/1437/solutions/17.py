import sys


def convert(x):
    if x >= 'A' and x <= 'Z':
        return (ord(x) - ord('A')) + 10
    if x >= 'a' and x <= 'z':
        return (ord(x) - ord('a')) + 36
    if x >= '0' and x <= '9':
        return (ord(x) - ord('0'))
    if x == '-':
        return 62
    return 63


def ones(n):
    r = 0
    while n != 0:
        n &= n - 1
        r += 1
    return r


def zeros(x):
    return 6 - ones(x)

# def zeros(x):
#     i=1
#     res=0
#     while i<=x:
#         if (i&x) ==0:
#             res+=1
#         i= i<<1
#     return res


def pow(a, b, mod=10**9 + 7):
    res = 1
    while b > 0:
        if (b & 1) == 0:
            a = (a * a) % mod
            b = b >> 1
        else:
            res = (res * a) % mod
            b -= 1
    return res


def main():
    x = sys.stdin.readline().rstrip()
    t = 0
    for s in x:
        v = convert(s)
        z = zeros(v)
        t += z

    print(pow(3, t))


main()

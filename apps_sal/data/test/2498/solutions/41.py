def lcm(a, b):
    return a // gcd(a, b) * b


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def cnt(a):
    res = 0
    while(a and a % 2 == 0):
        a //= 2
        res += 1
    return res


n, m = map(int, input().split())
A = list(map(int, input().split()))

l = 1
c = cnt(A[0])
for a in A:
    if cnt(a) != c or c == 0:
        print(0)
        return
    else:
        l = lcm(l, a // 2)
d = m // l
print((d + 1) // 2)

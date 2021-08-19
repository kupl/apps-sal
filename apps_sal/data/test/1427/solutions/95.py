def gcd(a: int, b: int):
    if a > b:
        c = a
        a = b
        b = c
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    GCD = gcd(a, b)
    return a * b // GCD


def lcm_of_all(v):
    tmp = v[0]
    for i in range(1, len(v)):
        tmp = lcm(tmp, v[i])
    return tmp


N = int(input())
liA = list(map(int, input().split()))
liB = [-1 for _ in range(N)]
G = lcm_of_all(liA)
MOD = 10 ** 9 + 7
ss = 0
for i in range(N):
    liB[i] = G // liA[i]
    ss += liB[i]
ss %= MOD
print(ss)

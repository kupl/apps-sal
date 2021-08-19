n = int(input())
l = list(map(int, input().split(' ')))


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


hoge = 1
for p in l:
    hoge = lcm(hoge, p)
ans = 0
for p in l:
    ans += hoge // p
print(ans % int(1000000000.0 + 7))

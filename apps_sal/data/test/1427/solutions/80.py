def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
numbers = list(map(int, input().split()))
l = numbers[0]
for i in range(1, n):
    l = lcm(l, numbers[i])
ans = 0
for i in range(n):
    ans += l // numbers[i]
MOD = 1000000007
print(ans % MOD)

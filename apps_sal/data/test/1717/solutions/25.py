n = int(input())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


ans = 1
for i in range(2, n + 1):
    ans = (ans * i) // gcd(ans, i)
print((ans + 1))

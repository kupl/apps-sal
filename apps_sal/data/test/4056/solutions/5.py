import math


def fnl(n):
    c = 0
    ln = (int)(math.sqrt(n))
    for i in range(1, ln + 1):
        if (n % i == 0):
            if(n / i == i):
                c += 1
            else:
                c += 2
    return c


N = int(input())
s = [int(x) for x in input().split()]
c = s[0]
for i in range(1, len(s)):
    c = math.gcd(c, s[i])

ans = fnl(c)
print(ans)

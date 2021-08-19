import math


def countDivisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):

            # If divisors are equal,
            # count only one
            if (n / i == i):
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2
    return cnt


x = int(input())
l = list(map(int, input().split()))
g = l[0]
for i in range(1, x):
    g = math.gcd(g, l[i])
print(countDivisors(g))

# t-=1

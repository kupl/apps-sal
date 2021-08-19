import math


def divisors(x):
    l = [[], []]
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i ** 2 != x:
                l[0].append(i)
                l[1].append(x // i)
            else:
                l[0].append(i)
    return l[0] + l[1][::-1]


def primenumber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


(a, b) = map(int, input().split())
cnt = 0
for i in divisors(math.gcd(a, b)):
    if i == 1:
        cnt += 1
    elif primenumber(i):
        cnt += 1
print(cnt)

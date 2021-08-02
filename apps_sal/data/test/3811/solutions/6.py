import math
from sys import exit as ex
# A function to print all prime factors of
# a given number n


def pf(n):
    l = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        l.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            l.append(i),
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        l.append(n)
    return (set(l))


n = int(input())
a, b = list(map(int, input().split()))
x = pf(a)
x = list(x.union(pf(b)))
dp = [1 for i in range(len(x))]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    t = False
    for j in range(len(x)):
        if a % x[j] == 0 or b % x[j] == 0:
            dp[j] += 1
for i in range(len(dp)):
    if dp[i] == n:
        print(x[i])
        ex()
print(-1)
ex()

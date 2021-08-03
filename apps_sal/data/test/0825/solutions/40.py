import collections
import sys
def input(): return sys.stdin.readline().rstrip()


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
count = 0
prime_list = collections.Counter(prime_factorize(N))

for key in prime_list:
    num = prime_list[key]
    for i in range(1, num + 1):
        if i <= num:
            num -= i
            count += 1
        else:
            break

print(count)

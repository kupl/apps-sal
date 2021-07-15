import collections

n = int(input())

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

if n == 1: # 1
    print((0))
    return

c = collections.Counter(prime_factorize(n))
_, counts = list(zip(*c.most_common()))

l = list(counts)
ans = 0

if l == [1]: # prime number
    print((1))
    return

for i in l:
    for j in range(1, i+1):
        if i >= j:
            i -= j
            ans += 1

print(ans)


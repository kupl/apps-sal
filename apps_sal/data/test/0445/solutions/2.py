from time import time
n = int(input())
a = list(map(int, input().split()))

start = time()

cache = {}


def is_prime(n):
    if n not in cache:
        cache[n] = _is_prime(n)

    return cache[n]


def _is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


s = {}
i = 0
while i < len(a):
    if a[i] > 1 and a[i] in s:
        a.pop(i)
    else:
        s[a[i]] = True
        i += 1

p = [0] * len(a)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if not is_prime(a[i] + a[j]):
            p[i] += 1
            p[j] += 1

while True:
    mx = max(p)
    if mx == 0:
        break

    mi = p.index(mx)

    for i in range(0, len(a)):
        if i == mi or not is_prime(a[mi] + a[i]):
            p[i] -= 1

    a.pop(mi)
    p.pop(mi)

print(len(a))
print(" ".join(map(str, a)))

#print(time() - start)


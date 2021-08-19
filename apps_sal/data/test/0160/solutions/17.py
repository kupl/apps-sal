(n, k) = map(int, input().split())
a = list(map(int, input().split()))
m = sum(a)


def divisor(n):
    ass = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ass.append(i)
            ass.append(n // i)
    return ass


f = divisor(m)
f.sort(reverse=True)
for p in f:
    b = [x % p for x in a]
    b.sort()
    t = 0
    c = n
    for x in b:
        if x + t > k:
            break
        t += x
        c -= 1
    if c * p - sum(b) + t <= k:
        print(p)
        break

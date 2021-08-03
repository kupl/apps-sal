[n, k] = [int(t) for t in input().split(' ')]
a = [int(t) for t in input().split(' ')]

mask = (1 << k) - 1


def c2(n):
    return (n * (n - 1)) // 2


count = {}
count[0] = 1

p = 0
for i in a:
    p = p ^ i
    p = min(p, p ^ mask)
    count[p] = count.get(p, 0) + 1

res = 0
for [_, cnt] in list(count.items()):
    k = cnt // 2
    res += c2(k) + c2(cnt - k)

print(c2(n + 1) - res)

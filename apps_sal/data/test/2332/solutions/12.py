def rd(): return list(map(int, input().split()))


n, k, m = rd()
a = input().split()
b = list(rd())
d = dict(list(zip(a, b)))
for _ in range(k):
    x = list(rd())[1:]
    m = min(b[i - 1] for i in x)
    for i in x:
        d[a[i - 1]] = m
print(sum([d[x] for x in input().split()]))

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = { }
d2 = { }
result = 0

for x in a:
    cur = d2.get(x)
    if cur is not None:
        result += cur
    cur = d.get(x)
    if cur is not None:
        d2[k * x] = d2.get(k * x, 0) + cur
    d[k * x] = d.get(k * x, 0) + 1

print(result)


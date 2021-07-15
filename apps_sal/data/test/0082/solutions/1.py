n, k = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))

s = sum(l)
total = len(l)
res = 0
while s < total*k - total/2:
    s += k
    total += 1
    res += 1

print(res)


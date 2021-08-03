input()
count = {}
for x in map(int, input().split()):
    d = 2
    while d * d <= x:
        if x % d == 0:
            count[d] = count.get(d, 0) + 1
            while x % d == 0:
                x //= d
        else:
            d += 1
    if x > 1:
        count[x] = count.get(x, 0) + 1
print(max([1] + list(count.values())))

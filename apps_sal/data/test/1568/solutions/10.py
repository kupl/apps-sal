def rd(): return list(map(int, input().split()))


n, a, b, c, t = rd()
y = list(rd())
print(sum([t * (c - b) + x * (b - c) + a for x in y]) if c > b else a * n)

a = int(input())
b = int(input())

res = list(range(b + 1, 0, -1))
res.extend(list(range(b + 2, a + b + 2)))
print(' '.join(map(str, res)))


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    c, d = divmod(b, a)
    res = 0
    for j in range(d):
        res += (c + 1) ** 2
    for j in range(a - d):
        res += c ** 2
    print(res)

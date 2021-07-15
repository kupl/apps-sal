a, b, c = map(int, input().split())

def sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x = x // 10
    return s
res = []
for i in range(1, 100):
    x = b * i ** a + c
    if x > 0 and x < 10 ** 9  and sum(x) == i:
        res.append(x)
res.sort()
print(len(res))
print(*res)

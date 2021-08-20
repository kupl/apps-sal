def R():
    return map(int, input().split())


a = int(input())
b = int(input())
if a > b:
    (a, b) = (b, a)
m = (a + b) // 2


def d(x):
    return x * (x + 1) // 2


print(d(m - a) + d(b - m))

def f(x):
    return (x if x < 10 else f(x // 10) + x % 10)


n, s = map(int, input().split())
x = s
while x - f(x) < s:
    x += 1
print(max(0, n - x + 1))

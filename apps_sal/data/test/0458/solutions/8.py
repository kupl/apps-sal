def f(y):
    m = 0
    while y > 0:
        m += y % 10
        y = y // 10
    return m


a, b, c = map(int, input().split())
ans = []
x = 1
while x < 82:
    k = b * (x**a) + c
    if k < 10**9 and f(k) == x:
        ans.append(k)
    x += 1
print(len(ans))
if len(ans):
    print(*ans)

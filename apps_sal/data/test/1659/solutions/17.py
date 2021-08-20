ans = 0
(n, x) = list(map(int, input().split()))
for i in range(n):
    (c, y) = input().split()
    y = int(y)
    if c == '+':
        x += y
    elif x >= y:
        x -= y
    else:
        ans += 1
print(x, ans)

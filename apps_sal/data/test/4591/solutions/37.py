(a, b, c, x, y) = list(map(int, input().split()))
sum = a + b
if x > y:
    cost = a
else:
    cost = b
if sum > 2 * c:
    if x == y:
        total = 2 * x * c
        pass
    else:
        total = 2 * min(x, y) * c
        num = max(x, y) - min(x, y)
        if cost * num < 2 * num * c:
            total += cost * num
        else:
            total += 2 * num * c
elif sum == 2 * c:
    if x == y:
        total = x * 2 * c
        pass
    else:
        total = min(x, y) * 2 * c
        num = max(x, y) - min(x, y)
        if cost * num < 2 * c * num:
            total += cost * num
        else:
            total += num * 2 * c
else:
    total = a * x + b * y
print(total)

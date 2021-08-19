n = int(input())
ans = 0
l = 2 * n - 2
for x in range(0, l - n + 1):
    t = 4
    for y in range(0, l):
        if x <= y and y < x + n:
            continue
        elif y == x - 1 or y == x + n:
            t *= 3
        else:
            t *= 4
    ans += t
print(ans)

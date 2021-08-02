n = int(input())
x = int(((1 + 4 * 2 * (n + 1))**0.5 - 1) / 2)
if (x + 1) * (x + 2) <= (n + 1) * 2:
    x += 1
if x * (x + 1) > (n + 1) * 2:
    x -= 1
ans = n + 1 - x
print(ans)

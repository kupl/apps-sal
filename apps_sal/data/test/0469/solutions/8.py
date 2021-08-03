r, h = map(int, input().split())

half_count = (2 * h + r) // (2 * r)

res = 2 * half_count

x1 = 0
y1 = h + r / 2

x2 = r / 2
y2 = (r * (2 * half_count - 1)) / 2

if (x1 - x2) ** 2 + (y1 - y2) ** 2 >= r * r:
    res += 1

print(res)

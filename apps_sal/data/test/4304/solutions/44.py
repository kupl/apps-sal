(a, b) = map(int, input().split())
c = b - a
for i in range(1, 999):
    x = (i + 1) * i // 2
    y = (i + 2) * (i + 1) // 2
    if y - x == c:
        print(x - a)
        break

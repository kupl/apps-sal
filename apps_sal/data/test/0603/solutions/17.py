r, g, b = list(map(int, input().split()))

md = 0

for i in range(3):
    d = i
    if r < i or g < i or b < i:
        break
    d += (r - i) // 3
    d += (g - i) // 3
    d += (b - i) // 3
    md = max(md, d)

print(md)


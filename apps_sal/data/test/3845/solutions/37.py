a, b = list(map(int, input().split()))
a -= 1
b -= 1
ans = [["#" for _ in range(90)] for _ in range(40)] + [["." for _ in range(90)] for _ in range(40)]
pos = 0
for i in range(a):
    x = pos % 90
    y = (pos // 90) * 2
    ans[y][x] = "."
    pos += 2

pos = 0
for j in range(b):
    x = pos % 90
    y = 45 + (pos // 90) * 2
    ans[y][x] = "#"
    pos += 2

print((80, 90))
for row in ans:
    print(("".join(row)))

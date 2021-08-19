(x1, y1, x2, y2) = map(int, input().split())
ans1 = ((x2 - x1) // 2 + 1) * ((y2 - y1) // 2 + 1)
x1 += 1
y1 += 1
x2 -= 1
y2 -= 1
ans2 = 0
if x1 <= x2 and y1 <= y2:
    ans2 = ((x2 - x1) // 2 + 1) * ((y2 - y1) // 2 + 1)
print(ans1 + ans2)

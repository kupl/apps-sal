x, y = map(int, input().split())
x1, y1 = map(int, input().split())
ans1 = abs(x - x1) + 1
ans2 = abs(y - y1) + 1
if x == x1 or y == y1:
    ans1 += 1
print(ans1 * 2 + ans2 * 2)

(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
ans = 2 * (abs(x1 - x2) + abs(y1 - y2) - 1) + 6
if x1 == x2 or y1 == y2:
    ans += 2
print(ans)

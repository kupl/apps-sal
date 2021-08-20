(x, y) = list(map(int, input().split()))
(fx, fy) = list(map(int, input().split()))
ans = 0
if x == fx or y == fy:
    ans = 2
ans += abs(fx - x) * 2 + abs(fy - y) * 2 + 4
print(ans)

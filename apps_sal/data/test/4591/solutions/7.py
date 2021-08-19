def LI():
    return list(map(int, input().split()))


(a, b, c, x, y) = LI()
ans = float('INF')
for i in range(max(x, y) + 1):
    ans = min(ans, a * max(0, x - i) + b * max(0, y - i) + c * 2 * i)
print(ans)

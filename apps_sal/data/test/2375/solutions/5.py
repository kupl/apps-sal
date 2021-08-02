x, y = list(map(int, input().split()))

if abs(x - y) <= 1:
    ans = "Brown"
else:
    ans = "Alice"

print(ans)

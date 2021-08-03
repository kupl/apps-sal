x, y = map(int, input().split())

ans = "No"

for i in range(x + 1):
    if 2 * i + 4 * (x - i) == y:
        ans = "Yes"

print(ans)

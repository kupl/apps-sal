x, a, b = map(int, input().split())

if b - a <= 0:
    ans = "delicious"
elif b - a <= x:
    ans = "safe"
else:
    ans = "dangerous"

print(ans)

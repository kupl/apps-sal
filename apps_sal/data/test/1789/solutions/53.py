a, b, x, y = map(int, input().split())

if a > b:
    ans = min(((a - b)*2 - 1)*x, (a - b - 1)*y + x)
elif a == b:
    ans = x
else:
    ans = min(((b - a)*2 + 1)*x, (b - a)*y + x)

print(ans)

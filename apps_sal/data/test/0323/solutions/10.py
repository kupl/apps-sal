a, b = map(int, input().split())

x = min(a, b)

ans = 1

for i in range(x):
    ans *= (i + 1)

print(ans)

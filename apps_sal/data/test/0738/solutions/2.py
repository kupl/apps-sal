a, b, c, d = map(int, input().split())

ans = 0

ru = [0] * (10 ** 6 + 10)
for x in range(a, b + 1):
    l = x + b
    r = x + c + 1
    ru[l] += 1
    ru[r] -= 1
for i in range(10 ** 6 + 9):
    ru[i + 1] += ru[i]

for i in range(10 ** 6 + 9):
    ru[i + 1] += ru[i]

ans = 0
for z in range(c, d + 1):
    ans += ru[-1] - ru[z]

print(ans)

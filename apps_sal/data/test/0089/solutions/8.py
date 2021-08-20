n = int(input())
ar = []
for x in range(0, n + 1):
    for y in range(x + 1, n + 1):
        ar.append([x, y])
ans = 0
for x in ar:
    if x[0] <= (n + 1 - n % 2) / 2 <= x[1]:
        ans += 1
print(ans)

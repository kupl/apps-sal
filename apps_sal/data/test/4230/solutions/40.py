x, n = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    if p[i] - x >= 0:
        p[i] = 2 * (p[i] - x)
    else:
        p[i] = (x - p[i]) * 2 - 1
p = sorted(p)
i = 0
while i in p:
    i += 1
if i % 2 == 0:
    j = round(i / 2) + x
else:
    j = x - round((i + 1) / 2)
print(j)

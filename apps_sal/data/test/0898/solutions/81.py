(n, m) = list(map(int, input().split()))
yakusuu = []
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        yakusuu.append(m // i)
        if m // i == i:
            continue
        yakusuu.append(i)
ans = 0
for y in yakusuu:
    if y < n:
        continue
    if m % y == 0:
        ans = max(ans, m // y)
print(ans)

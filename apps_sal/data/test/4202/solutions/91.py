L, R = (int(x) for x in input().split())
if R - L > 2019 * 2:
    R -= ((R - L) // 2019 - 1) * 2019
ans = 2019
for i in range(L, R):
    for j in range(i + 1, R + 1):
        ans = min(ans, (i * j) % 2019)
print(ans)

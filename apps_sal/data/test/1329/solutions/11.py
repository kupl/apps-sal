
# 75 = 5 * 5 * 3
# 3 * 5 * 5, 3 * 25, 5 * 15, 75


n = int(input())

div = [0] * (n + 1)
for i in range(2, n + 1):
    j = 2
    while j * j <= i:
        while i % j == 0:
            div[j] += 1
            i //= j
        j += 1
    if i != 1:
        div[i] += 1

i3 = i5 = i15 = i25 = i75 = 0
for _, v in enumerate(div):
    if v >= 74:
        i75 += 1
    if v >= 24:
        i25 += 1
    if v >= 14:
        i15 += 1
    if v >= 4:
        i5 += 1
    if v >= 2:
        i3 += 1
ans = i75
ans += i25 * (i3 - 1)
ans += i15 * (i5 - 1)
ans += (i5 - 1) * i5 // 2 * (i3 - 2)
print(ans)

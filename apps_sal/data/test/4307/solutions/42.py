N = int(input())
ans = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    num = 0
    for j in range(1, i + 1):
        if i % j == 0:
            num += 1
    if num == 8:
        ans += 1
print(ans)

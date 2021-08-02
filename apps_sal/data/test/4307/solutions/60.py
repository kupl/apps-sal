n = int(input())

ans = 0
for i in range(1, n + 1, 2):
    t = 0
    if i <= 17: continue
    for j in range(1, n + 1, 2):
        if i % j == 0: t += 1
    if t == 8: ans += 1
print(ans)

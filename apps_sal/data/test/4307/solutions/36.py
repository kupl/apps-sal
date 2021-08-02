n = int(input())

if n < 17:
    print(0)
    return

ans = 0
for i in range(1, n + 1, 2):
    t = 0
    for j in range(1, i + 1, 2):
        if i % j == 0:
            t += 1
    if t == 8:
        ans += 1
print(ans)

x = int(input())
ans = 1
for i in range(2, x):
    if i * i > x:
        break
    now = i
    while now * i <= x:
        now *= i
    if now > ans:
        ans = now
print(ans)

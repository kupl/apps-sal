a = [int(input()) for _ in range(5)]
z = 123
ans = 0
for i in a:
    if i % 10 != 0:
        z = min(z, i % 10)
    ans += 10 * ((i + 10 - 1) // 10)
print(ans + z - 10 if (z != 123) or (z == 0) else ans)

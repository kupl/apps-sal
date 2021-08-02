x, y, z = list(map(int, input().split()))
ans = 0
for i in range(1, x):
    kt = x - i
    ans = max(ans, min(y // i, z // kt))
print(ans)

n, m, z = list(map(int, input().split()))
ans = 0
for i in range(1, z + 1):
    if i % m == 0 and i % n == 0:
        ans += 1
print(ans)

n, a, b, c = list(map(int, input().split()))
ans = int(1e18)
for i in range(4):
    for j in range(2):
        for k in range(4):
            if (n + i + 2 * j + 3 * k) % 4 == 0:
                ans = min(ans, i * a + j * b + k * c)
print(ans)


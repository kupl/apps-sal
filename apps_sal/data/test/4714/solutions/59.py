(a, b) = map(int, input().split())
ans = 0
for i in range(a // 10000, b // 10000 + 1):
    for j in range(0, 10):
        for k in range(0, 10):
            x = i * 10001 + j * 1010 + k * 100
            if a <= x <= b:
                ans += 1
print(ans, flush=True)

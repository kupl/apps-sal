x = int(input())
ans = 1000000
for b in range(1, 32):
    for p in range(2, 10):
        if x - b ** p < 0:
            continue
        ans = min(ans, abs(x - b ** p))
print(x - ans)

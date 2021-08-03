K, S = list(map(int, input().split()))
ans = 0
for x in range(0, K + 1):
    for y in range(0, K + 1):
        z = S - x - y
        if 0 <= z and z <= K:
            ans += 1
print(ans)

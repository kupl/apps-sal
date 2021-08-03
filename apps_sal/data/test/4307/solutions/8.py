N = int(input())
ans = 0

for n in range(1, N + 1):
    if n % 2:
        cnt = 0
        for m in range(1, n + 1):
            if n % m == 0:
                cnt += 1
        if cnt == 8:
            ans += 1

print(ans)

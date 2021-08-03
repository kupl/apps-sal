n, m = list(map(int, input().split()))
ans = 0
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0 and i <= m / n:
        if m // i <= m / n:
            ans = m // i
            break
        else:
            ans = i

print(ans)

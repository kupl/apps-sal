(C, Hr, Hb, Wr, Wb) = map(int, input().split())
ans = 0
for i in range(3 * 10 ** 5):
    if Wr * i <= C:
        ans = max(ans, Hr * i + (C - Wr * i) // Wb * Hb)
for i in range(3 * 10 ** 5):
    if Wb * i <= C:
        ans = max(ans, Hb * i + (C - Wb * i) // Wr * Hr)
print(ans)

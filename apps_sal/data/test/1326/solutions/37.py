n = int(input())

ans = 0
for j in range(1, n + 1):  # 割る数
    a = j  # 初項
    d = n // j  # 項数
    tmp = (a + (a * d)) * d // 2
    ans += tmp

print(ans)

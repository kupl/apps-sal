n = int(input())

ans = 0
s = 1
for a in range(1, int(n ** .5) + 1):
    div = n // a
    ans += ((div + 1) * div // 2 - s) * a * 2 + a * a
    s += a + 1

print(ans)

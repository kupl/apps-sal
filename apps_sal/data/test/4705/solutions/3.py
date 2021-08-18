n = int(input())

x = 800 * n

y = 0
if n >= 15:
    y = 200 * (n // 15)

ans = x - y
print(ans)

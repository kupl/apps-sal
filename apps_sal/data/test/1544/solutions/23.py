n = int(input())
ans = 0
t = n + 4
w = 5
q = 1
while (w > 0):
    q *= t
    t -= 1
    w -= 1
ans = q // 120
ans *= n * (n + 1) * (n + 2)
ans = ans // 6
print(ans)

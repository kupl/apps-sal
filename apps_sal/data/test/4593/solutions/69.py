x = int(input())

ans = 0
for i in range(1, 100):
    for j in range(2, 100):
        y = pow(i, j)
        if y <= x:
            ans = max(ans, y)

print(ans)

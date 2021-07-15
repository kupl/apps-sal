X, Y, Z = list(map(int, input().split()))
if X - Y - 2 * Z < 0:
    print((0))
    return
X = X - Y - 2 * Z
ans = 1
for i in range(10 ** 5):
    if X - Y - Z >= 0:
        X = X - Y - Z
        ans += 1
        continue
    else:
        break
print(ans)


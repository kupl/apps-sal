N, X = map(int, input().split())

ans = 0
for i in range(N, -1, -1):
    if X < 2**(i + 1) - 1:
        X -= 1
    elif X > 2 ** (i + 1) - 1:
        X -= 2 ** (i + 1) - 1
        ans += 2 ** i
    else:
        ans += 2 ** i
        break
    if X == 0:
        break


print(ans)

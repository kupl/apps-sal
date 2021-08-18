def fill(X, c, start):
    for i in range(X):
        q, r = divmod(i, 49)
        i = q * 2 + start
        j = r * 2 + 1 if q % 2 else r * 2 + 2
        ans[i][j] = c


A, B = map(int, input().split())
H, W = 100, 100
ans = [list("
fill(A - 1, ".", 1)
fill(B - 1, "
print(H, W)
[print("".join(row)) for row in ans]

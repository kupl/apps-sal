def f(w, n):
    if w >= 3 and w <= n + 1:
        return (w - 1) // 2
    elif w > n + 1 and w <= 2 * n - 1:
        return ((2 * n + 2) - w - 1) // 2
    else:
        return 0


n = int(input())
e = len(str(2 * n)) - 1
des = 10 ** e - 1
ans = 0
for i in range(1, 10):
    ans += f(i * 10 ** e - 1, n)
print(ans)

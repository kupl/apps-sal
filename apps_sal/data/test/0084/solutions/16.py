n = int(input())
le = len(str(n))
if n < 5:
    print(n * (n - 1) // 2)
elif str(n).count('9') == le:
    print(n // 2)
else:
    if n + n - 1 < int('9' * le):
        le -= 1
    ans = 0
    s = '9' * le
    for i in range(9):
        t = str(i) + s
        t = int(t)
        if t <= n + 1:
            ans += t // 2
        elif t <= n + n - 1:
            ans += 1 + (n + n - 1 - t) // 2
    print(ans)

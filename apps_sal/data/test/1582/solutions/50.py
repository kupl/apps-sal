N = int(input())

ans = 0
for i in range(1, N + 1):
    a = list(map(int, str(i)))
    x = a[0]
    y = a[-1]
    if x == y:
        ans += 1
    if y != 0:
        for j in (5, 4, 3, 2, 1):
            z = (y + 1) * (10**j)
            if z <= N:
                ans += 10**(j - 1)
            elif y * (10**j) + x <= N and N < z:
                s = N - y * (10**j)
                ans += int(s / 10)
                if N % 10 >= x:
                    ans += 1

print(ans)

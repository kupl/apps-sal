t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        i = 0
        while 10 ** i <= n:
            i += 1
        i -= 1
        k = 1
        ans = 0
        while int(str(k) * (i + 1)) <= n:
            k += 1
            ans += 1
        print(9 * i + ans)

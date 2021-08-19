t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2 or n == 3:
        print(-1)
        continue
    if n >= 4:
        ans = []
        if n % 4 == 0:
            for i in range(1, n + 1, 4):
                ans += [i + 1, i + 3, i, i + 2]
        else:
            d = n // 4 - 1
            cur = 1
            for i in range(d):
                ans += [cur + 1, cur + 3, cur, cur + 2]
                cur += 4
            if n % 4 == 1:
                ans += [cur + 1, cur + 3, cur, cur + 2, cur + 4]
            elif n % 4 == 2:
                ans += [cur, cur + 2, cur + 4, cur + 1, cur + 3, cur + 5]
            else:
                ans += [cur, cur + 3, cur + 1, cur + 5, cur + 2, cur + 4, cur + 6]
        print(*ans)

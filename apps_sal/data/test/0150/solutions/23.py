def check(n):
    if n == 2:
        return 1
    elif n > 2:
        k = int(n**0.5) + 1
        b = 0
        for j in range(2, k + 1):
            if n % j == 0:
                return 0
            else:
                continue
        return 1


n = int(input())
if n == 2:
    print(1)
else:
    if n % 2 == 0:
        print(2)
    else:
        i = 0
        ans = 0
        while n > 2 and n - i >= 2:
            if check(n - i) == 1 and i != 1:
                n = i
                ans += 1
                i = 0
            else:
                i += 1
        print(min(ans + n // 2, 3))

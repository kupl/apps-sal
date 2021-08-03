n = int(input())
if n == 1:
    print("1")
elif n == 2:
    print("1 2")
else:
    base = 1
    gap = 2
    cur = base
    next = 1
    ans = ''
    for i in range(n - 1):
        ans += str(base) + ' '
        next = cur
        cur += gap
        if cur > n:
            base *= 2
            gap *= 2
            cur = base
        next = max(next, cur)
    ans += str(next)
    print(ans)

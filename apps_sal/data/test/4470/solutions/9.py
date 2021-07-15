q = int(input())
for q in range(q):
    n = int(input())
    ans = 0
    while (n != 1):
        if n % 5 == 0:
            n = n // 5 * 4
        elif n % 3 == 0:
            n = n // 3 * 2
        elif n & 1 == 0:
            n >>= 1
        else:
            break
        ans += 1
    if n != 1:
        print(-1)
    else:
        print(ans)


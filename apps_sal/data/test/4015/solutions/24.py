(n, m) = map(int, input().split())
if m % n != 0:
    print(-1)
else:
    m //= n
    ans = 0
    while m % 2 == 0:
        m //= 2
        ans += 1
    while m % 3 == 0:
        m //= 3
        ans += 1
    if m > 1:
        print(-1)
    else:
        print(ans)

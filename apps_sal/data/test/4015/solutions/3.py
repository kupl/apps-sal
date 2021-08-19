(n, m) = list(map(int, input().split()))
if m % n != 0:
    print(-1)
else:
    x = m // n
    ans = 0
    while x % 2 == 0:
        ans += 1
        x //= 2
    while x % 3 == 0:
        ans += 1
        x //= 3
    if x != 1:
        print(-1)
    else:
        print(ans)

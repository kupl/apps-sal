n = int(input())

if n % 2 == 1:
    print(0)
else:
    m = n // 2
    ans = 0
    while m > 0:
        ans += m // 5
        m = m // 5
    print(ans)

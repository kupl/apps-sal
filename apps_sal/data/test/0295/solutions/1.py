def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    (gcd, x1, y1) = egcd(b % a, a)
    x = y1 - b // a * x1
    y = x1
    return (gcd, x, y)


def main():
    n = int(input())
    div = []
    d = set()
    m = n
    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
            d.add(i)
        if cnt > 0:
            div.append((cnt, i))
        i += 1
    if n > 1:
        div.append((1, n))
        d.add(n)
    for i in d:
        if i == m:
            d.remove(i)
            break
    if len(d) < 2:
        print('NO')
        return
    ans1 = 1
    for i in range(div[0][0]):
        ans1 *= div[0][1]
    ans2 = 1
    for i in div[1:]:
        for j in range(i[0]):
            ans2 *= i[1]
    (gcd, x, y) = egcd(ans2, -ans1)
    if x < 0 or y < 0:
        (gcd, x, y) = egcd(ans1, -ans2)
        (x, y) = (y, x)
    print('YES')
    print(2)
    if ans2 * x + ans1 * y == m - 1:
        print(x, ans1)
        print(y, ans2)
    elif ans2 * (ans1 - x) + ans1 * y == m - 1:
        print(ans1 - x, ans1)
        print(y, ans2)
    elif ans2 * x + ans1 * (ans2 - y) == m - 1:
        print(x, ans1)
        print(ans2 - y, ans2)
    else:
        print(ans1 - x, ans1)
        print(ans2 - y, ans2)
    return


def __starting_point():
    main()


__starting_point()

def m():
    (n, p) = list(map(int, input().split()))
    now = 0
    s = input()
    if p == 2 or p == 5:
        ans = 0
        for i in range(n):
            if int(s[i]) % p:
                continue
            ans += i + 1
    else:
        table = [0] * p
        table[0] = 1
        c = 1
        for i in range(n - 1, -1, -1):
            now = (now + c * int(s[i])) % p
            c = 10 * c % p
            table[now] += 1
        ans = sum((j * (j - 1) // 2 for j in table))
    print(ans)


def __starting_point():
    m()


__starting_point()

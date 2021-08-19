for i in range(int(input())):
    n = input()
    m = len(n)
    ans = 9 * (m - 1)
    n = int(n)
    ans += int('1' * m) <= n
    ans += int('2' * m) <= n
    ans += int('3' * m) <= n
    ans += int('4' * m) <= n
    ans += int('5' * m) <= n
    ans += int('6' * m) <= n
    ans += int('7' * m) <= n
    ans += int('8' * m) <= n
    ans += int('9' * m) <= n
    print(ans)

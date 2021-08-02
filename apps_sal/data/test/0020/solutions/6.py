t = input()

ans = 0

while(t != t[::-1]):
    h, m = map(int, t.split(':'))

    m += 1
    h += m // 60
    m %= 60
    h %= 24

    ans += 1
    t = "{}{}:{}{}".format(str(h // 10), str(h % 10), str(m // 10), str(m % 10))

print(ans)

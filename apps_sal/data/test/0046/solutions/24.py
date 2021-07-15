n, m = map(int, input().split())
zer1 = n // 5
zer2 = m // 5
one1 = (n - 1) // 5 + 1
one2 = (m - 1) // 5 + 1
two1 = (n - 2) // 5 + 1
two2 = (m - 2) // 5 + 1
three1 = (n - 3) // 5 + 1
three2 = (m - 3) // 5 + 1
four1 = (n - 4) // 5 + 1
four2 = (m - 4) // 5 + 1
print(zer1 * zer2 + one1 * four2 + two1 * three2 + three1 * two2 + four1 * one2)

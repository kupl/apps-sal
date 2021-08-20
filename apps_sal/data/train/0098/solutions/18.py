n = int(input())
for i in range(n):
    (c, m, x) = list(map(int, input().split()))
    wynik = 0
    wynik += min(c, m, x)
    huj = min(c, m, x)
    c -= huj
    m -= huj
    x -= huj
    if x > 0:
        print(wynik)
    else:
        if c > m:
            (c, m) = (m, c)
        wynik += min(m, c, (m + c) // 3)
        print(wynik)

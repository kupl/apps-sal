n = int(input())
a = list(map(int, input().split()))
wynik = 0
if n < 3:
    wyn = a[0]
    for i in range(1, n):
        wyn = wyn | a[i]
    print(wyn)
else:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                wynik = max(wynik, a[i] | a[j] | a[k])
    print(wynik)

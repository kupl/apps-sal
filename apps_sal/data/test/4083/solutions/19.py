n, k = map(int, input().split())
l = list(map(int, input().split()))
d = {}
for liczba in l:
    ll = liczba
    while ll > 0:
        d[ll] = []
        ll //= 2
for liczba in l:
    i = 0
    ll = liczba
    while ll > 0:
        d[ll].append(i)
        ll //= 2
        i += 1
wyn = 1000000000
for number in d:
    if len(d[number]) < k:
        continue
    a = d[number].copy()
    a.sort()
    wyn = min(wyn, sum(a[:k]))
print(wyn)

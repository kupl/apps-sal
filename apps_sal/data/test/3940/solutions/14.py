from itertools import cycle, islice
(n, m) = [int(x) for x in input().split()]
dlzky = []
for _ in range(m):
    (a, b) = input().split()
    c = int(b) - int(a) + 1
    dlzky.append(c)
minimum = min(dlzky)
cisla = [str(x) for x in range(minimum)]
vysledok = islice(cycle(cisla), n)
print(minimum)
print(' '.join(vysledok))

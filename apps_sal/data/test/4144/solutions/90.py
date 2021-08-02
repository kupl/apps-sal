n = int(input())
waru = 1000000000 + 7


def kaijo(x, n):
    kake = 1
    for i in range(n):
        kake = (kake * x) % waru
    return kake


amari = kaijo(10, n) - 2 * kaijo(9, n) + kaijo(8, n)
amari %= waru
print(amari)

n, m, k = list(map(int, input().split()))
rad = (k - 1) // (2 * m) + 1
parta = ((k - 1) % (2 * m)) // 2 + 1
if (k % 2) == 0:
    print(rad, parta, "R")
else:
    print(rad, parta, "L")


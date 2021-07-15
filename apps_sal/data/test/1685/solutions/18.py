n, m = map(int, input().split())
for i in range(m):
    k = int(input())
    d = k & -k
    for q in input():
        if q == 'U' and k != n + 1 >> 1:
            k += d if (k + d) % (d << 2) else -d
            d <<= 1
        if q in 'LR' and d > 1:
            d >>= 1
            k += d if q == 'R' else -d
    print(k)

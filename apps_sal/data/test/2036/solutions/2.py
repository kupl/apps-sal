(n, m, x, y) = list(map(int, input().split()))
ii = y
print(x, y)
for c in range(1, m + 1):
    if y != c:
        print(x, c)
        ii = c
for r in range(1, n + 1):
    if x != r:
        print(r, ii)
        ij = 0
        for c in range(1, m + 1):
            if ii != c:
                print(r, c)
                ij = c
        ii = ij



n, m, k, x, y = list(map(int, input().split()))

if n != 1:
    full_rounds = k // (2 * (n - 2) * m + 2 * m)

    k %= (2 * (n - 2) * m + 2 * m)

    A = [[0 for j in range(m)] for i in range(n)]

    row = 0
    col = 0

    while k != 0 and row < n and col < m:
        A[row][col] += 1
        k -= 1
        col += 1
        if col == m:
            row += 1
            col = 0

    row = n - 2
    col = 0
    while k != 0:
        A[row][col] += 1
        k -= 1
        col += 1
        if col == m:
            row -= 1
            col = 0

    small = 10**18
    big = 0

    if x == n or x == 1:
        serg = full_rounds + A[x - 1][y - 1]
    else:
        serg = 2 * full_rounds + A[x - 1][y - 1]

    for row in A[1:-1]:
        small = min([small] + [2 * full_rounds + a for a in row])
        big = max([big] + [2 * full_rounds + a for a in row])

    small = min([small] + [full_rounds + a for a in A[0]])
    big = max([big] + [full_rounds + a for a in A[0]])

    small = min([small] + [full_rounds + a for a in A[-1]])
    big = max([big] + [full_rounds + a for a in A[-1]])

    print(str(big) + " " + str(small) + " " + str(serg))

else:
    A = [k // m] * m
    k %= m
    i = 0
    while k != 0:
        A[i] += 1
        k -= 1
        i += 1

    small = 10**18
    big = 0

    serg = A[y - 1]
    small = min([small] + A)
    big = max([big] + A)

    print(str(big) + " " + str(small) + " " + str(serg))

n, m = list(map(int, input().split()))
grid = []
d = {}
flags = 0
for i in range(n):
    grid.append(input())
for j in range(m):
    b = 0
    while b < n - 1:
        i = b
        k = i
        while k < n and grid[k][j] == grid[i][j]:
            k += 1
        c1 = k - i
        clr1 = grid[k - 1][j]
        i = k
        if 2 * c1 <= n - k:
            while k < n and grid[k][j] == grid[i][j]:
                k += 1
            c2 = k - i
            clr2 = grid[k - 1][j]
            i = k
            if c1 == c2 and c2 <= n - k:
                while k < n and grid[k][j] == grid[i][j]:
                    k += 1
                    if k - i == c2:
                        break
                c3 = k - i
                clr3 = grid[k - 1][j]
                if c3 == c2:
                    flags += 1
                    if (c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1) in d and \
                            d[(c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1)][1] == (j - 1):
                        flags += d[(c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1)][0]
                        d[(c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1)][1] = j
                        d[(c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1)][0] += 1
                    else:
                        d[(c3, clr1, clr2, clr3, k - 2 * c3 - 1, k - 1)] = [1, j]
        b += 1
print(flags)


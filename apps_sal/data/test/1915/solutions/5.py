def d(i, j):
    if i == 1 or j == 1:
        return 1
    return d(i - 1, j) + d(i, j - 1)


n = int(input())
print(d(n, n))

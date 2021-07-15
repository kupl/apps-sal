def a(i, j):
    if i == 1 or j == 1:
        return 1
    return a(i - 1, j) + a(i, j - 1)

n = int(input())
print(a(n, n))

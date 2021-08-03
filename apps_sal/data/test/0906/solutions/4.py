n, m, k = list(map(int, input().split()))
diag = n + m - 2
if k == -1 and diag % 2 == 1:
    print(0)
else:
    print(pow(2, (n - 1) * (m - 1), 10 ** 9 + 7))

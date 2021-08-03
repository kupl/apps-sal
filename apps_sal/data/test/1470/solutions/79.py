x = int(input())
n = x // 11
m = x % 11
if 0 < m <= 6:
    print(n * 2 + 1)
elif 7 <= m:
    print(n * 2 + 2)
elif m == 0:
    print(2 * n)

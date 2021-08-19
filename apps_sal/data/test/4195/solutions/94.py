(d, n) = map(int, input().split())
if n <= 99:
    print(100 ** d * n)
else:
    print(101 * 100 ** d)

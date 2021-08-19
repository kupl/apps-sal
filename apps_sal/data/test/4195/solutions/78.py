(d, n) = list(map(int, input().split()))
if n < 100:
    print(pow(100, d) * n)
else:
    print(pow(100, d) * 101)

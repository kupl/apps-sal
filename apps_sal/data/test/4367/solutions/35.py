(n, k) = map(int, input().split())
if n >= 10:
    print(k)
else:
    print(k + (10 - n) * 100)

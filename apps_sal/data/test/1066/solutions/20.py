n, k = list(map(int, input().split()))
a = (n + 1) // 2
if (k <= a):
    print(k * 2 - 1)
else:
    print((k - a) * 2)

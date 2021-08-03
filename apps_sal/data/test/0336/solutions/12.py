n, a, b, c, d = list(map(int, input().split()))
lst = [a + b, a + c, c + d, b + d]
if (n - (max(lst) - min(lst))) <= 0:
    print(0)
else:
    print((n - (max(lst) - min(lst))) * n)

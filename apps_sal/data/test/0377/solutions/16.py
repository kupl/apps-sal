n, m = list(map(int, input().split()))
if m * 2 <= n and m != 0:
    print(m)
elif m == 0:
    print(1)
else:
    print(n - m)

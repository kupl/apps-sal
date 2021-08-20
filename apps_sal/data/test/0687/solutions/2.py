(n, m) = list(map(int, input().split()))
if n == m - 1:
    print(n, m)
elif n == m:
    print(n * 10, n * 10 + 1)
elif n == 9 and m == 1:
    print(9, 10)
else:
    print(-1)

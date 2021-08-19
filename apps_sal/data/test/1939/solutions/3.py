(n, k) = map(int, input().split())
for i in range(n):
    if i != n - 1:
        print(*[0] * (n - i - 1), end=' ')
    print(k, end=' ')
    print(*[0] * i)

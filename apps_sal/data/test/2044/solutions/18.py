(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
bal = 0
for i in range(n):
    print((bal + a[i]) // m, end=' ')
    bal = (bal + a[i]) % m

(k, n, s, p) = list(map(int, input().split()))
one = (n + s - 1) // s
print((one * k + p - 1) // p)

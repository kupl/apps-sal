k, n, s, p = map(int, input().split())
x = (n + s - 1) // s
print((x * k + p -1) // p)

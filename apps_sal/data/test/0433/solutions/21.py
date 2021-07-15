(n, a, b) = map(int, input().split())
k = (a + b) % n
print(k if k != 0 else n)

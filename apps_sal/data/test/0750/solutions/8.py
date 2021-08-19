(n, k) = map(int, input().split())
r = (n * 2 + k - 1) // k
g = (n * 5 + k - 1) // k
b = (n * 8 + k - 1) // k
print(r + b + g)

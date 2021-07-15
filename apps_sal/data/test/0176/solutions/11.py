k, a, b = map(int, input().split())
a += k * 10**18 + k
b += k * 10**18 + k
print(b // k - (a - 1) // k)

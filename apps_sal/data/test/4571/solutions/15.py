a, b = map(int, input().split())
c = 2**b
A = 100 * (a - b)
B = 1900 * b
print((A + B) * c)

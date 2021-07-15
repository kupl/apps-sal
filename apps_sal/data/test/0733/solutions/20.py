3

x, y, a, b = tuple(map(int, input().split()))

def gcd(i, j):
    while i:
        i, j = j % i, i
    return j

s = x * y // gcd(x, y)
print(b // s - (a - 1) // s)


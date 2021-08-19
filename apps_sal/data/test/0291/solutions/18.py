(a, b) = list(map(int, input().split()))
n = 0
while a <= b:
    a *= 3
    b *= 2
    n += 1
print(n)

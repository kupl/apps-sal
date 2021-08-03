a, b = list(map(int, input().split()))

y = 0
while(a <= b):
    y += 1
    a *= 3
    b *= 2

print(y)

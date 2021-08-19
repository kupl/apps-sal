(a, b) = map(int, input().split())
b *= 2
if a <= b:
    print(0)
else:
    print(a - b)

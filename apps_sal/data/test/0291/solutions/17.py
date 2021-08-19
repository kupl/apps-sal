(a, b) = map(int, input().split())
i = 0
while True:
    i += 1
    a *= 3
    b *= 2
    if a > b:
        break
print(i)

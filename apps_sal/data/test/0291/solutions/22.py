(a, b) = [int(x) for x in input().split(' ')]
c = 0
while b >= a:
    c += 1
    a *= 3
    b *= 2
print(c)

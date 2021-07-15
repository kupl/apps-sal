a, b, c = map(int, input().split())

count = 0
while not (a == b == c):
    count += 1
    a, b, c = sorted([a, b, c])
    if a == b:
        a += 1
        b += 1
    else:
        a += 2
print(count)

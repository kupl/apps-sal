(h, a) = list(map(int, input().split()))
count = 0
while h > 0:
    h -= a
    count += 1
    if h <= 0:
        break
print(count)

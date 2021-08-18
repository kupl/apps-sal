
[h, a] = list(map(int, input().split()))

count = 0
while h > 0:
    count += 1
    h -= a

print(count)

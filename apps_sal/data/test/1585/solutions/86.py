x, y = map(int, input().split())

count = 0
while y >= x:
    count += 1
    y = y // 2
print(count)

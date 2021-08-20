(x, y) = map(int, input().split())
count = 1
while x * 2 <= y:
    count += 1
    x *= 2
print(count)

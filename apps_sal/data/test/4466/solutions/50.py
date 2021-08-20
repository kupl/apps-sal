a = list(map(int, input().split()))
x = 0
count = 0
while a[0] - a[2] >= x:
    x += a[1]
    x += a[2]
    count += 1
print(count - 1)

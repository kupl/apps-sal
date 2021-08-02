X = int(input())

count = 0
n = 100
while n < X:
    n += n // 100
    count += 1
else:
    print(count)

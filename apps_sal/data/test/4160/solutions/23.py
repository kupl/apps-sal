x = int(input())
a = 100
count = 0
while a < x:
    a += a // 100
    count += 1
print(count)

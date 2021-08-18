a = int(input())

count = 0

if int(a / 100) == 1:
    count += 1

if int(a / 10 % 10) == 1:
    count += 1

if int(a % 100 % 10) == 1:
    count += 1

print(count)

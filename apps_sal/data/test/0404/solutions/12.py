b = int(input())
cur = 1
count = 0
while cur*cur <= b:
    if b%cur == 0:
        count += 2
    if cur*cur == b:
        count -= 1
    cur += 1
print(count)


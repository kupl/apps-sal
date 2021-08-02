n = int(input())
count = 0
while n > 0:
    n -= int(max(str(n)))
    count += 1
print(count)

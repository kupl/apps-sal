b = int(input())
count = 0
i = 1
while i * i <= b:
    if b % i == 0:
        count += 2
        if i * i == b:
            count -= 1
    i += 1
print(count)

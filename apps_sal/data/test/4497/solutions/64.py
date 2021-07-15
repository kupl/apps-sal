n = int(input())
max_count, answer = 0, 0
for i in range(1, n + 1):
    num = i
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1
    if count > max_count:
        max_count, answer = count, i

print((max(1, answer)))


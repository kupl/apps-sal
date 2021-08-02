n, a, b = map(int, input().split())
count = 0
for i in range(1, n + 1):
    num = i
    digit = 0
    while num > 0:
        digit += num % 10
        num = num // 10
    if a <= digit <= b:
        count += i
print(count)

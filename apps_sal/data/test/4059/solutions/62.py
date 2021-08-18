
n = int(input())

count = 0
max_divisor_n = n // 2
for a in range(1, n):
    for b in range(1, a + 1):
        if a * b >= n:
            break
        count += 1
        if a != b:
            count += 1
print(count)

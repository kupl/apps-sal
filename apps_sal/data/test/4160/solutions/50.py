n, count, k = 100, 0, int(input())
while n < k:
    n += n // 100
    count += 1
print(count)

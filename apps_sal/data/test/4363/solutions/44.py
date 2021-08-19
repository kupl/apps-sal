(k, s) = map(int, input().split())
total = 0
for i in range(k + 1):
    for j in range(k + 1):
        gen = s - k
        num = i + j
        if num <= s and num >= gen:
            total += 1
print(total)

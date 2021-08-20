(k, s) = map(int, input().split(' '))
count = 0
for i in range(k + 1):
    for j in range(k + 1):
        if i + j <= s and s <= k + i + j:
            count += 1
print(count)

n = int(input())
res = 0
count = 0
for i in range(1, 100000):
    res += sum((j for j in range(1, i + 1)))
    if res <= n:
        count += 1
    else:
        break
print(count)

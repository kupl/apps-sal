n = int(input())
count = 0
for i in range(n + 1):
    if i % 2 != 0:
        count += 1

print(float(count / n))

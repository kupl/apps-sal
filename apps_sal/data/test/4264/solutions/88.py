n = int(input())
count = 0
for i in range(1, n + 1):
    s = str(i)
    if len(s) % 2 != 0:
        count += 1
print(count)

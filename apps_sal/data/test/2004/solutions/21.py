n = int(input())
print(str(n + n // 2))
for i in range(n + 1):
    if i == 0 or i % 2 == 1:
        continue
    print(str(i) + ' ', end='')
for i in range(n + 1):
    if i == 0 or i % 2 == 0:
        continue
    print(str(i) + ' ', end='')
for i in range(n + 1):
    if i == 0 or i % 2 == 1:
        continue
    print(str(i) + ' ', end='')

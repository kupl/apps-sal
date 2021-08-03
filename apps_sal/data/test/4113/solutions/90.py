n = int(input())

c = 0
for i in range(0, n // 4 + 1):
    for j in range(0, n // 7 + 1):
        if 4 * i + 7 * j == n:
            c += 1

if c == 0:
    print('No')
else:
    print('Yes')

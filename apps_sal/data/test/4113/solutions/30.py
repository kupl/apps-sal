result = False
n = int(input())
for i in range(n // 4 + 1):
    for j in range(n // 7 + 1):
        if 4 * i + 7 * j == n:
            result = True
            break
if result:
    print('Yes')
else:
    print('No')

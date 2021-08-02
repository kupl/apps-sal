n = int(input())

for i in range(n):
    j = 0
    while 4 * i + 7 * j <= 100:
        if 4 * i + 7 * j == n:
            print('Yes')
            return
        else:
            j += 1
print('No')

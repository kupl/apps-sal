n = int(input())
x = 100 // 7 + 2
for i in range(x):
    for j in range(x):
        if 4 * i + 7 * j == n:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')

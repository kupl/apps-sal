n = int(input())
count = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            print('Yes')
            count = 1
            break
    if count == 1:
        break
if count == 0:
    print('No')

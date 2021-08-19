n = int(input())
check = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            check = True
print('Yes' if check else 'No')

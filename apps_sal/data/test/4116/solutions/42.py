n = int(input())
y = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            y += 1
        else:
            pass
if y >= 1:
    print('Yes')
else:
    print('No')

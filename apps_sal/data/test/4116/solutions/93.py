n = int(input())
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            cnt += 1
if cnt == 0:
    print('No')
else:
    print('Yes')

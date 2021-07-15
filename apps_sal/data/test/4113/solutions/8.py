n = int(input())
cnt = 0
for i in range(30):
    for j in range(20):
        price = 4 * i + 7 * j
        if price == n:
            cnt += 1
if cnt == 0:
    print('No')
else:
    print('Yes')

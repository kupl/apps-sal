n = int(input())
neg = 0
pos = 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    if x < 0:
        neg += 1
    else:
        pos += 1
if neg < 2 or pos < 2:
    print('Yes')
else:
    print('No')

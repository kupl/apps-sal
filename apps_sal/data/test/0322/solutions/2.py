left = 0
right = 0
n = int(input())
for i in range(n):
    (x, y) = map(int, input().split())
    if x > 0:
        right += 1
    else:
        left += 1
if right <= 1 or left <= 1:
    print('Yes')
else:
    print('No')

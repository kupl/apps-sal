n = list(map(int, input('').strip().split()))[0]
left = 0
right = 0
for i in range(n):
    (x, y) = list(map(int, input('').strip().split()))
    if x < 0:
        left += 1
    else:
        right += 1
if left <= 1 or right <= 1:
    print('Yes')
else:
    print('No')

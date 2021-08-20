def R():
    return map(int, input().split())


n = int(input())
left = 0
right = 0
for i in range(n):
    (a, b) = R()
    if a > 0:
        right += 1
    if a < 0:
        left += 1
if min(left, right) < 2:
    print('Yes')
else:
    print('No')

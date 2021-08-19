n = int(input())
m = 0
x = 0
for i in range(n):
    (a, b) = map(int, input().split())
    if a == b:
        x += 1
    else:
        x = 0
    m = max(x, m)
if m >= 3:
    print('Yes')
else:
    print('No')

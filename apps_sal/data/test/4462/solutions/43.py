n = int(input())
a = list(map(int, input().split()))
x = 0
y = 0
for i in range(n):
    if a[i] % 2 != 0:
        x += 1
    elif a[i] % 4 == 0:
        y += 1
if x <= y:
    print('Yes')
elif x + y == n and x == y + 1:
    print('Yes')
else:
    print('No')

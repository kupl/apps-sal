n = int(input())
count = 0
an = 0
for i in range(n):
    (d1, d2) = map(int, input().split())
    if d1 == d2:
        count += 1
    else:
        count = 0
    if count == 3:
        an = 1
if an == 1:
    print('Yes')
else:
    print('No')

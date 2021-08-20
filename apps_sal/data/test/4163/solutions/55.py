n = int(input())
count = 0
judge = False
for _ in range(n):
    (d1, d2) = [int(x) for x in input().split()]
    if d1 == d2:
        count += 1
        if count >= 3:
            judge = True
    else:
        count = 0
if judge:
    print('Yes')
else:
    print('No')

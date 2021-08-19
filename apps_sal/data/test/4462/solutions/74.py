n = int(input())
A = list(map(int, input().split()))
(d, q, x) = (0, 0, 0)
for a in A:
    if a % 4 == 0:
        q += 1
    elif a % 2 == 0:
        d += 1
    else:
        x += 1
x += d % 2
d -= d % 2
if q + 1 >= x:
    print('Yes')
else:
    print('No')

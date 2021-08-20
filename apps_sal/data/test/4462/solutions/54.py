n = int(input())
a = list(map(int, input().split()))
(b, c, d) = (0, 0, 0)
for i in a:
    if i % 4 == 0:
        b += 1
    elif i % 2 == 0:
        c += 1
    else:
        d += 1
if c == 0 and b >= d - 1:
    print('Yes')
elif b >= d:
    print('Yes')
else:
    print('No')

n = eval(input())
l = list(map(int, input().split()))
(c1, c2) = (0, 0)
for x in l:
    if x & 1 == 0:
        c1 += 1
    else:
        c2 += 1
if c1 > c2:
    print('READY FOR BATTLE')
else:
    print('NOT READY')

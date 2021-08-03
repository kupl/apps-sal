n = int(input())
a = 0
ok = False
for i in range(0, n):
    x, y = list(map(int, input().split()))
    if x == y:
        a = a + 1
        if a >= 3:
            ok = True
    else:
        a = 0
if ok:
    print('Yes')
else:
    print('No')

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [b[i] - a[i] for i in range(n)]
    last = None
    fail = False
    if any((x < 0 for x in c)):
        fail = True
    for item in c:
        if last == None:
            if item == 0:
                continue
            else:
                last = item
        elif item == 0:
            last = 0
        elif item != last:
            fail = True
            break
    if fail:
        print('NO')
    else:
        print('YES')

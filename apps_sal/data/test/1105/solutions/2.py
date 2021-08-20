n = int(input())
tasks = {}
fail = False
for i in range(n):
    (x, k) = list(map(int, input().split()))
    if k not in tasks:
        if x == 0:
            tasks[k] = {x}
        else:
            fail = True
            break
    elif x == 0:
        if x in tasks[k]:
            tasks[k].add(x)
        else:
            fail = True
            break
    elif x > 0:
        if x - 1 in tasks[k]:
            tasks[k].add(x)
        else:
            fail = True
            break
    else:
        fail = True
        break
if fail:
    print('NO')
else:
    print('YES')

(a, b, c) = list(map(int, input().split()))
if a == 1 or b == 1 or c == 1:
    print('YES')
elif a == 3 and b == 3 and (c == 3):
    print('YES')
else:
    l = {}
    l[2] = 0
    l[4] = 0
    l[a] = 0
    l[b] = 0
    l[c] = 0
    l[a] += 1
    l[b] += 1
    l[c] += 1
    if l[2] >= 2:
        print('YES')
    elif l[2] == 1 and l[4] == 2:
        print('YES')
    else:
        print('NO')

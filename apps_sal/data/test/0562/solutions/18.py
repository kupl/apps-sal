n = int(input())
t = []
flag = True
for i in range(n):
    t.append(list(map(int, input().split(' '))))
t.sort()
(l1, l2) = (-1, -1)
for i in range(n):
    if t[i][0] > l1 and t[i][0] > l2:
        if l1 > l2:
            l1 = t[i][1]
        else:
            l2 = t[i][1]
    elif t[i][0] > l1:
        l1 = t[i][1]
    elif t[i][0] > l2:
        l2 = t[i][1]
    else:
        print('NO')
        flag = False
        break
if flag:
    print('YES')

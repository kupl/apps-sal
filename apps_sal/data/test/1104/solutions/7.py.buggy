n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


if a[0] >= b[0]:
    for x in range(4):
        for y in range(4):
            if (x | y) == a[0] and (x & y) == b[0]:
                t = [x, y]
                ans = 1
                for i in range(1, n - 1):
                    if a[i] >= b[i]:
                        flag = 0
                        for ti in range(4):
                            if (t[i] | ti == a[i]) and (t[i] & ti) == b[i]:
                                t.append(ti)
                                flag = 1
                        if flag == 0:
                            ans = 0
                            break
                    else:
                        ans = 0
                        break

                if ans == 1:
                    print('YES')
                    print(*t)
                    return
    print('NO')


else:
    print('NO')

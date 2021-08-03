# WARNING This code is just for fun. Reading it might give u a brainfreeze

n, d, k = [int(x) for x in input().strip().split(' ')]
l = []
i = 1
if n <= d:
    print("NO")
elif k == 1:
    if n > 2:
        print("NO")
    elif n == 2:
        print("YES")
        print(1, 2)
else:
    n += 1
    flag = False
    while i < min(d + 1, n):
        l.append(str(i) + " " + str(i + 1))
        i += 1
    i += 1
    cnt1 = 0
    cnt2 = 1
    se = [[2, d + 1, 1]]
    while cnt1 < cnt2:
        start = se[cnt1][0]
        end = se[cnt1][1]
        mode = se[cnt1][2]
        # print(se)
        kk = 3
        while (i < n) and (kk <= k):
            if i < n and not flag:
                j = start
                # print(j,"kk")
                while i < n and j < end:
                    if mode == 1:
                        c = min(j - start + 1, end - j)
                    else:
                        c = min(end - j, d - end + j)
                    if c > 1:
                        se.append([i, i + c - 1, 2])
                        cnt2 += 1
                    ki = j
                    while i < n and c > 0:
                        l.append(str(ki) + " " + str(i))
                        # print(j,i,c)
                        c -= 1
                        ki = i
                        i += 1
                    j += 1

            else:
                flag = True
                break
            kk += 1
        cnt1 += 1
    if i < n or flag:
        # print(l)
        print("NO")
    else:
        print("YES")
        print('\n'.join(l))

def solo_mid(n, x0, y0, sturms=[]):
    if n == 0:
        return 0
    res = {}
    for i in range(n):
        for_shot = sturms[:]
        first_sturm = for_shot[0]
        sturms.remove(first_sturm)
        line_x = y0 - first_sturm[1]
        line_y = -(x0 - first_sturm[0])
        line_c = -first_sturm[0] * line_x + first_sturm[1] * -line_y
        res[first_sturm] = 1
        for (xi, yi) in for_shot[1:]:
            is_in_line = line_x * xi + line_y * yi + line_c
            if is_in_line == 0:
                res[first_sturm] += 1
                sturms.remove((xi, yi))
        if not sturms:
            break
    return len(res)


try:
    first = input()
    if len(first.split()) != 3:
        print(0)
    else:
        in_f = [int(i) for i in first.split()]
        n = in_f[0]
        sturms = []
        for i in range(n):
            s = input()
            if len(s.split()) != 2:
                print(0)
                break
            else:
                try:
                    s_l = tuple([int(i) for i in s.split()])
                except:
                    break
                sturms.append(s_l)
        else:
            print(solo_mid(n, in_f[1], in_f[2], sturms))
except:
    print(0)

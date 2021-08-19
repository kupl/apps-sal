def build(a0, a1, a01, a10, arr):
    while True:
        if a0 + a1 == 0 and a01 + a10 > 0:
            return (False, '')
        if a01 < a1 and a10 < a0:
            return (False, '')
        if a01 + a10 == 0:
            if a0 > 0 and a1 > 0:
                return (False, '')
            while a0 > 0:
                arr.append(0)
                a0 -= 1
            while a1 > 0:
                arr.append(1)
                a1 -= 1
            return (True, arr)
        if a01 >= a1:
            arr.append(0)
            a0 -= 1
            a01 -= a1
        else:
            arr.append(1)
            a1 -= 1
            a10 -= a0


val = [0] * 50000
for i in range(1, 50000):
    val[i] = i * (i - 1) // 2
d = {x: i for (i, x) in enumerate(val)}
(a00, a01, a10, a11) = map(int, input().split())


def solve(a00, a01, a10, a11):
    a0_arr = []
    a1_arr = []
    ans = None
    flag = False
    if a00 == 0:
        a0_arr = [0, 1]
    else:
        if a00 not in d:
            return (flag, ans)
        a0_arr.append(d[a00])
    if a11 == 0:
        a1_arr = [0, 1]
    else:
        if a11 not in d:
            return (flag, ans)
        a1_arr.append(d[a11])
    for a0 in a0_arr:
        for a1 in a1_arr:
            arr = []
            (flg, arr) = build(a0, a1, a01, a10, arr)
            if flg == True:
                flag = flg
                ans = arr
                break
    return (flag, ans)


(flag, ans) = solve(a00, a01, a10, a11)
if flag == False:
    print('Impossible')
else:
    print(''.join([str(x) for x in ans]))

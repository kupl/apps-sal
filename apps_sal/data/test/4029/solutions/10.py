l = [int(e) for e in input().strip()]


def lei00(l):
    result = []
    for i in range(len(l) - 1, -1, -1):
        if l[i] == 0:
            result.append(i)
        if len(result) == 2:
            break
    if len(result) < 2:
        return None
    return 2 * len(l) - result[0] - result[1] - 3


def lei(l, x, y):
    assert x != y
    ix = None
    iy = None
    for i in range(len(l) - 1, -1, -1):
        if l[i] == x and ix == None:
            ix = i
        elif l[i] == y and iy == None:
            iy = i
        if ix != None and iy != None:
            break
    if ix == None or iy == None:
        return None
    result = 2 * len(l) - ix - iy - 3
    if ix > iy:
        result += 1
    if x == 7 or x == 2:
        assert y == 5
        if iy == 0 and l[1] == 0:
            if len(l) >= 4:
                iii = 1
                while True:
                    iii += 1
                    if l[iii] != 0:
                        break
                result += iii - 1
            if len(l) == 3:
                return None
    return result


l = [lei00(l), lei(l, 5, 0), lei(l, 7, 5), lei(l, 2, 5)]
result = None
for e in l:
    if e == None:
        continue
    if result == None or result > e:
        result = e
if result == None:
    print(-1)
else:
    print(result)

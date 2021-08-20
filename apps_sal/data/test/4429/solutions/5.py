t = int(input())


def fun(x, y, z):
    a = -1
    b = -1
    c = -1
    flag = 0
    l = [x, y, z]
    for i in l:
        for j in l:
            for k in l:
                if x == max(i, j) and y == max(i, k) and (z == max(j, k)):
                    flag = 1
                    a = i
                    b = j
                    c = k
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print('YES')
        print(a, b, c)
    else:
        print('NO')


while t:
    t -= 1
    (x, y, z) = list(map(int, input().split()))
    fun(x, y, z)

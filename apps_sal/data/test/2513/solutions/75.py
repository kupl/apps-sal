import sys
n = int(input())
s = str(input())
l = [0] * n
flag = 1
if s[0] == 'x':
    flag = 0
    new_s = ''
    for j in range(n):
        if s[j] == 'x':
            new_s += 'o'
        else:
            new_s += 'x'
    s = new_s


def check(i, l):
    sys.setrecursionlimit(10000000)
    if i == 0:
        l11 = [0] * n
        l12 = [0] * n
        l21 = [0] * n
        l22 = [0] * n
        l11[0] = 'S'
        l11[1] = l11[n - 1] = 'S'
        l12[0] = 'S'
        l12[1] = l12[n - 1] = 'W'
        tmp1 = check(i + 1, l11)
        tmp2 = check(i + 1, l12)
        l21[0] = l21[n - 1] = 'W'
        l21[1] = 'S'
        l22[0] = l22[1] = 'W'
        l22[n - 1] = 'S'
        tmp3 = check(i + 1, l21)
        tmp4 = check(i + 1, l22)
        if tmp1 == tmp2 == tmp3 == tmp4 == -1:
            return -1
        else:
            if tmp1 != -1:
                return tmp1
            if tmp2 != -1:
                return tmp2
            if tmp3 != -1:
                return tmp3
            if tmp4 != -1:
                return tmp4
    elif 1 <= i <= n - 2:
        if s[i] == 'o':
            if l[i] == 'S':
                l[i + 1] = l[i - 1]
                return check(i + 1, l)
            elif l[i - 1] == 'W':
                l[i + 1] = 'S'
                return check(i + 1, l)
            else:
                l[i + 1] = 'W'
                return check(i + 1, l)
        elif l[i] == 'W':
            l[i + 1] = l[i - 1]
            return check(i + 1, l)
        elif l[i - 1] == 'S':
            l[i + 1] = 'W'
            return check(i + 1, l)
        else:
            l[i + 1] = 'S'
            return check(i + 1, l)
    elif s[i] == 'o':
        if l[i] == 'S':
            if l[i - 1] == l[0]:
                if l[0] == 'W' and l[i] == l[1] or (l[0] == 'S' and l[i] != l[1]):
                    return -1
                else:
                    return l
            else:
                return -1
        elif l[i - 1] != l[0]:
            if l[0] == 'W' and l[i] == l[1] or (l[0] == 'S' and l[i] != l[1]):
                return -1
            else:
                return l
        else:
            return -1
    elif l[i] == 'S':
        if l[i - 1] != l[0]:
            if l[0] == 'W' and l[i] == l[1] or (l[0] == 'S' and l[i] != l[1]):
                return -1
            else:
                return l
        else:
            return -1
    elif l[i - 1] == l[0]:
        if l[0] == 'W' and l[i] == l[1] or (l[0] == 'S' and l[i] != l[1]):
            return -1
        else:
            return l
    else:
        return -1


ans = check(0, l)
if ans == -1:
    print(-1)
elif flag:
    print(''.join(ans))
else:
    for i in range(n):
        if ans[i] == 'S':
            ans[i] = 'W'
        else:
            ans[i] = 'S'
    print(''.join(ans))

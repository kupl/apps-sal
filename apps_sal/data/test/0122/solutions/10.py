n = int(input())
a = list(map(int, input().split()))
s = sum(a)


def solve(a):
    rtn = False
    tmp = 0
    dic = {}
    for i in range(n):
        tmp += a[i]
        dic[a[i]] = True
        if tmp == s // 2:
            rtn = True
            break
        elif s // 2 < tmp and (tmp - s // 2) in dic:
            rtn = True
            break
    return rtn


if n == 1 or s % 2 == 1:
    print('NO')
elif solve(a) or solve(list(reversed(a))):
    print('YES')
else:
    print('NO')


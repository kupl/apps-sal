n = int(input())
l = list(map(int, input().split()))
l.sort()


def ok(l):
    for i in range(len(l)):
        if l[i - 1] >= l[i - 2] + l[i]:
            return False
    return True


if ok(l):
    print('YES')
    print(*l)
else:
    l[-3:] = l[-2:] + l[-3:-2]
    if ok(l):
        print('YES')
        print(*l)
    else:
        print('NO')

x, y = list(map(int, input().split()))
l = [y, y, y]


def arg():
    argmax = 0
    argmin = 0
    for i in range(1, 3):
        if l[i] > l[argmax]:
            argmax = i
        if l[i] < l[argmin]:
            argmin = i
    if argmax == argmin:
        argmax = 0
        argmin = 1
    tmp = [0, 1, 2]
    tmp.remove(argmax)
    tmp.remove(argmin)
    return (argmin, tmp[0], argmax)


cnt = 0
while l[0] != x or l[1] != x or l[2] != x:
    args = arg()
    l[args[0]] = min(x, l[args[2]] + l[args[1]] - 1)
    cnt += 1
print(cnt)

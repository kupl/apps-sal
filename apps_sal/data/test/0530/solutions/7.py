def ii():
    return int(input())


def kk():
    return map(int, input().split())


def ll():
    return list(kk())


(n, a1, a2) = (ii(), input(), input())
locs = [0] * 4
for i in range(2 * n):
    locs[int(a1[i]) + 2 * int(a2[i])] += 1
rm = min(locs[1], locs[2])
locs[1] -= rm
locs[2] -= rm
locs[3] = locs[3] & 1
if locs[1]:
    print('First')
elif locs[3]:
    if locs[2] == 0:
        print('First')
    elif locs[2] < 3:
        print('Draw')
    else:
        print('Second')
elif locs[2] < 2:
    print('Draw')
else:
    print('Second')

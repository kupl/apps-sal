3


def readln(): return tuple(map(int, input().split()))


n, = readln()
cnt = [0, 0]
for v in readln():
    if v == 25:
        cnt[0] += 1
    elif v == 50:
        if cnt[0]:
            cnt[0] -= 1
            cnt[1] += 1
        else:
            cnt = None
            break
    else:
        if cnt[0] and cnt[1]:
            cnt[0] -= 1
            cnt[1] -= 1
        elif cnt[0] > 2:
            cnt[0] -= 3
        else:
            cnt = None
            break
print('YES' if cnt else 'NO')

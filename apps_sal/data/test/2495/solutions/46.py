n = int(input())
a = list(map(int, input().split()))


def calc(tmp, cnt=0):
    for i in a[1:]:
        if tmp < 0:
            tmp = tmp + i
            if tmp <= 0:
                cnt += -tmp + 1
                tmp = 1
        elif tmp > 0:
            tmp = tmp + i
            if tmp >= 0:
                cnt += tmp + 1
                tmp = -1
    return cnt


if a[0]:
    hugou = 1 if a[0] > 0 else -1
    print(min(calc(a[0]), calc(-hugou, abs(a[0]) + 1)))
else:
    print(min(calc(1, 1), calc(-1, 1)))

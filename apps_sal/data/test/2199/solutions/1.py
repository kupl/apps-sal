import sys
input = sys.stdin.readline

Q = int(input())
a = []
sm = []


def best():
    mx = a[-1]
    n = len(a)
    l, r = 0, n - 2
    ret = mx
    while l <= r:
        mid = (l + r) // 2
        s = sm[mid] + mx
        c = mid + 2
        avg = s / c
        if a[mid] > avg:
            r = mid - 1
        else:
            ret = avg
            l = mid + 1
    return ret


for _ in range(Q):
    inp = [int(i) for i in input().split()]
    if len(inp) == 2:
        x = inp[1]
        a.append(x)
        sm.append((sm[-1] if sm else 0) + x)
    else:
        mx = a[-1]
        avg = best()
        ans = mx - avg
        print(ans)

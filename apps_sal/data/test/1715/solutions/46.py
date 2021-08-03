import bisect
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
s.sort()
t = [int(input()) for i in range(b)]
t.sort()

"""
sとtのどちらを先にするか
左右どちらに走るか
の都合4パターンの最小値を選べばよい
"""


def minl(x):
    # sを選択
    idx = bisect.bisect_left(s, x)
    ret = 3 * 10**10
    if idx == 0:
        first = s[0] - x
        now = s[0]
        idx = bisect.bisect_left(t, now)
        if idx == 0:
            second = t[0] - now
        elif idx == b:
            second = now - t[b - 1]
        else:
            second = min(now - t[idx - 1], t[idx] - now)
        ret = min(ret, first + second)
    elif idx == a:
        first = x - s[a - 1]
        now = s[a - 1]
        idx = bisect.bisect_left(t, now)
        if idx == 0:
            second = t[0] - now
        elif idx == b:
            second = now - t[b - 1]
        else:
            second = min(now - t[idx - 1], t[idx] - now)
        ret = min(ret, first + second)
    else:
        for first_g in [s[idx - 1], s[idx]]:
            first = abs(first_g - x)
            now = first_g
            idx = bisect.bisect_left(t, now)
            if idx == 0:
                second = t[0] - now
            elif idx == b:
                second = now - t[b - 1]
            else:
                second = min(now - t[idx - 1], t[idx] - now)
            ret = min(ret, first + second)

    # tを選択
    idx = bisect.bisect_left(t, x)
    if idx == 0:
        first = t[0] - x
        now = t[0]
        idx = bisect.bisect_left(s, now)
        if idx == 0:
            second = s[0] - now
        elif idx == a:
            second = now - s[a - 1]
        else:
            second = min(now - s[idx - 1], s[idx] - now)
        ret = min(ret, first + second)
    elif idx == b:
        first = x - t[b - 1]
        now = t[b - 1]
        idx = bisect.bisect_left(s, now)
        if idx == 0:
            second = s[0] - now
        elif idx == a:
            second = now - s[a - 1]
        else:
            second = min(now - s[idx - 1], s[idx] - now)
        ret = min(ret, first + second)
    else:
        for first_g in [t[idx - 1], t[idx]]:
            first = abs(first_g - x)
            now = first_g
            idx = bisect.bisect_left(s, now)
            if idx == 0:
                second = s[0] - now
            elif idx == a:
                second = now - s[a - 1]
            else:
                second = min(now - s[idx - 1], s[idx] - now)
            ret = min(ret, first + second)
    return ret


for i in range(q):
    x = int(input())
    print(minl(x))

import sys
(a1, a2, a3, a4, a5, a6) = map(int, input().split())


def calc(h):
    res = 0
    cur = 1
    while cur <= h:
        res += cur + cur - 1
        cur += 1
    return res


ax1 = a4
ax2 = a6
ans = calc(ax1 + ax2 + a5) - calc(ax1) - calc(ax2) - calc(a2)
print(ans)

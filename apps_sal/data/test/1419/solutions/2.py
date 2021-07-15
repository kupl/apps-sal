import sys

inf = 1 << 30

def solve():
    def check(mid):
        if a_max > mid:
            return False

        tot = 1
        line = 0

        for ai in a:
            if line + ai > mid:
                tot += 1
                line = ai

                if tot > k:
                    return False
            else:
                line += ai

        return True

    k = int(input())
    s = input().replace('-', ' ')

    a = [len(si) + 1 for si in s.split()]
    a[-1] -= 1
    a_max = max(a)

    top = len(s)
    btm = 0

    while top - btm > 1:
        mid = (top + btm) // 2

        if check(mid):
            top = mid
        else:
            btm = mid

    ans = top

    print(ans)

def __starting_point():
    solve()
__starting_point()

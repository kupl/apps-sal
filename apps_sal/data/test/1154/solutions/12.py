3


def main():
    n, h, k = list(map(int, input().split()))
    dat = list(map(int, input().split()))

    ptr = 0
    t = 0
    cur = 0
    while ptr != len(dat):
        if cur + dat[ptr] > h:
            mindecr = cur + dat[ptr] - h
            dt = (mindecr + k - 1) // k
            t += dt

            cur = max(0, cur - dt * k)
            continue

        while ptr != len(dat) and cur + dat[ptr] <= h:
            cur += dat[ptr]
            ptr += 1
        cur = max(0, cur - k)
        t += 1
    t += (cur + k - 1) // k
    print(t)


main()

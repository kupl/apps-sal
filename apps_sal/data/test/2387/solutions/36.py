def check(ar):
    h = 0
    for bottom, up in ar:
        if h + bottom < 0:
            return False
        h += up
    return True


def __starting_point():
    N = int(input())
    pos = []
    neg = []
    equal = 0
    for _ in range(N):
        cnt = 0
        bottom = 0
        for s in input():
            if s == "(":
                cnt += 1
            else:
                cnt -= 1
            bottom = min(bottom, cnt)
        equal += cnt
        if cnt >= 0:
            pos.append((bottom, cnt))
        else:
            cnt = -cnt
            bottom += cnt
            neg.append((bottom, cnt))

    pos.sort(reverse=True)
    neg.sort(reverse=True)
    if check(pos) and check(neg) and equal == 0:
        print("Yes")
    else:
        print("No")


__starting_point()

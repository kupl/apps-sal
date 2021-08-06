import sys
input = sys.stdin.readline


def main():
    N = int(input())
    s = sorted(list(map(int, input().strip().split())), reverse=True)
    check = [False] * (2**N)
    now = []
    now.append([s[0], 1])
    check[0] = True
    ok = True
    for i in range(N):
        next_ = []
        tmp = 0
        for j in range(len(now)):
            hp, start = now[j]
            start = max(start, tmp)
            ok = False
            for k in range(start, 2**N):
                if s[k] < hp and not check[k]:
                    tmp = k + 1
                    now[j][1] = k + 1
                    check[k] = True
                    next_.append([s[k], k + 1])
                    ok = True
                    break
            if not ok:
                break
        now += next_
        now = sorted(now, reverse=True)
        if not ok:
            break

    if ok:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()

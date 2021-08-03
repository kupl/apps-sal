from sys import stdin
input = stdin.readline


def main():
    N = int(input())
    R = [tuple(map(int, input().split())) for _ in range(N)]
    B = [tuple(map(int, input().split())) for _ in range(N)]

    num_friends = 0
    B.sort(key=lambda x: x[0])

    for ib, b in enumerate(B):
        bx, by = b[0], b[1]

        tmp_r = (-1, -1)

        for ir, r in enumerate(R):
            rx, ry = r[0], r[1]

            if rx < bx and \
               ry < by and \
               tmp_r[1] < ry:
               # b[0] - r[0] < tmp_b[0] - r[0] and \
               # b[1] - r[1] < tmp_b[1] - r[1]:
                tmp_r = r

        if tmp_r == (-1, -1):
            continue
        num_friends += 1
        R.remove(tmp_r)

    print(num_friends)


if(__name__ == '__main__'):
    main()

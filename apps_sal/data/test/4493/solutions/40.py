# coding: utf-8


def main():
    ans = 'No'
    c = [list(map(int, input().split())) for _ in range(3)]
    for i in range(101):
        for j in range(101):
            for k in range(101):
                flgs = [False, False, False]
                if c[0][0] - i == c[1][0] - j and c[0][0] - i == c[2][0] - k:
                    flgs[0] = True
                if c[0][1] - i == c[1][1] - j and c[0][1] - i == c[2][1] - k:
                    flgs[1] = True
                if c[0][2] - i == c[1][2] - j and c[0][2] - i == c[2][2] - k:
                    flgs[2] = True
                if (all(flgs)):
                    ans = 'Yes'

    print(ans)


def __starting_point():
    main()


__starting_point()

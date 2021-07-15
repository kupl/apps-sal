
def main():

    L, R = [int(i) for i in input().split()]

    if (L//2019) < (R//2019):
        ans = 0
    else:
        ans = 10 ** 10
        for l in range(L, R+1):
            for r in range(l+1, R+1):
                ans = min(ans, (l*r)%2019)

    print(ans)


def __starting_point():
    main()
__starting_point()

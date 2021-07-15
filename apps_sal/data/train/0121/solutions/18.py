def main():
    def solve():

        n = int(input())
        aa = [int(a) for a in input().split()]
        aa.sort()
        print(aa[n] - aa[n-1])

    q = int(input())
    for _ in range(q):
        solve()


def __starting_point():
    main()
__starting_point()

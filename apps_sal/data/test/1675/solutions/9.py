def main():
    n = int(input())
    teams = [input().split() for _ in range(n)]
    home = dict()
    ans = list()

    for i in range(n):
        home[teams[i][0]] = home.get(teams[i][0], 0) + 1

    print('\n'.join('{} {}'.format(n - 1 + home.get(teams[i][1], 0),
            n - 1 - home.get(teams[i][1], 0)) for i in range(n)))

def __starting_point():
    main()
__starting_point()

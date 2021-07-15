def main():
    n = int(input())
    teams = [list(map(int, input().split())) for _ in range(n)]
    home = [0] * ((10 ** 5) + 1)
    ans = list()

    for i in range(n):
        home[teams[i][0]] += 1

    print('\n'.join('{} {}'.format(n - 1 + home[teams[i][1]], n - 1 - home[teams[i][1]]) for i in range(n)))

def __starting_point():
    main()
__starting_point()

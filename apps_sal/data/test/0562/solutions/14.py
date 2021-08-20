n = int(input())
shows = []
for i in range(n):
    shows.append([int(x) for x in input().split()])
shows = sorted(shows, key=lambda tup: tup[0])


def fit(show, tv):
    if show[1] < tv[0] or show[0] > tv[1]:
        return True
    return False


def main():
    if n < 2:
        print('YES')
        return
    tv1 = shows[0]
    tv2 = shows[1]
    for show in shows[2:]:
        if fit(show, tv1):
            tv1 = show
        elif fit(show, tv2):
            tv2 = show
        else:
            print('NO')
            return
    print('YES')
    return


main()

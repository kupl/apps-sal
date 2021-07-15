class C:
    def c(self, n, m):
        total = n+m
        noofteams = int(total/3)
        if noofteams > n:
            noofteams = n
        elif noofteams > m:
            noofteams = m
        return noofteams


def __starting_point():
    values = input().split(' ', 2)
    print(C().c(int(values[0]), int(values[1])))
__starting_point()

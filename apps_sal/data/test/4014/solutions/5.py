# Hello World program in Python
class exam:
    def __init__(self, tickets, ex_day, prep_days, index):
        self.tick = tickets - 1
        self.ex_day = ex_day - 1
        self.prep_days = prep_days
        self.index = index


def task():
    n, m = [int(x) for x in input().split(' ')]
    exs = list()
    for i in range(m):
        a, b, c = [int(x) for x in input().split(' ')]
        exs.append(exam(a, b, c, i + 1))
    s = sum((x.prep_days for x in exs))
    if s > n - m:
        print(-1)
        return -1
    exs = sorted(exs, key=lambda x: -x.tick)
    exdays = [x.ex_day for x in exs]
    days = [m + 1 if i in exdays else 0 for i in range(0, n)]
    for ex in exs:
        d = ex.ex_day
        offs = 1
        for i in range(ex.prep_days):
            cont = True
            while (cont):
                if d - offs < ex.tick:
                    print(-1)
                    return
                if days[d - offs] == 0:
                    days[d - offs] = ex.index
                    cont = False
                else:
                    offs += 1

    print(' '.join((str(x) for x in days)))


task()

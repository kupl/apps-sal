class Worker():
    def __init__(self, j, c):
        self.job = j
        self.cost = c


def read(type=1):
    if type:
        file = open("input.dat", "r")
        line = list(map(int, file.readline().split()))
        a = list(map(int, file.readline().split()))
        b = list(map(int, file.readline().split()))
        file.close()
    else:
        line = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
    c = []
    for i in range(line[0]):
        c.append(Worker(a[i], b[i]))
    return line[0], line[1], c


def solve():
    sols = [0 for i in range(k)]
    c = sorted(a, key=lambda x: x.cost, reverse=True)
    jobs = 0
    mins = []
    for i in range(n):
        if sols[c[i].job - 1]:
            mins.append(c[i].cost)
        else:
            jobs += 1
            sols[c[i].job - 1] = 1
    sol = 0
    for i in range(k - jobs):
        sol += mins[len(mins) - i - 1]
    return sol


n, k, a = read(0)
sol = solve()
print(sol)

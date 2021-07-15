def read(type = 1):
    if type:
        file = open("input.dat", "r")
        n = int(file.readline())
        line = list(map(int, file.readline().split()))
        file.close()
    else:
        n = int(input().strip())
        line = list(map(int, input().strip().split()))
    return n, line


def solve():
    MOD = 998244353
    sol = 0.5
    ranges = {}
    pos = 0
    for v in a:
        if v not in ranges:
            ranges[v] = (pos, pos)
        else:
            ranges[v] = (ranges[v][0], pos)
        pos += 1
    pos = 0
    ranges = list(ranges.items())
    i = 0
    while pos < n:
        while 1:
            if ranges[i][1][0] <= pos:
                if ranges[i][1][1] > pos:
                    pos = ranges[i][1][1]
                i += 1
                if i == len(ranges):
                    break
            else:
                break
        sol = int(2 * sol)
        sol %= MOD
        pos += 1
    return sol


n, a = read(0)
sol = solve()
print(sol)

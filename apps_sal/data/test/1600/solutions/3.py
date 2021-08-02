n = int(input())
hs = list(map(int, input().split()))


def solve(n, hs):
    mins = fill_mins(n, hs)
    maxs = fill_maxs(n, hs)
    count = 1
    for i in range(n - 1):
        if maxs[i] <= mins[i + 1]:
            count += 1
    return count


def fill_mins(n, hs):
    mins = []
    tmp = float('inf')
    for h in hs[::-1]:
        if h < tmp:
            tmp = h
        mins.append(tmp)
    mins.reverse()
    return mins


def fill_maxs(n, hs):
    maxs = []
    tmp = 0
    for h in hs:
        if h > tmp:
            tmp = h
        maxs.append(tmp)
    return maxs


print(solve(n, hs))

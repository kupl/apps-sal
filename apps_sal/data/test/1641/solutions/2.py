import sys


def roadToCinema(V, S, T, stations):
    """
    V       : volume of fuel tank
    S       : total distance
    T       : time limit
    stations: fuel stations' locations

    rtype   : boolean, whether this aircraft can travel within the time limit
    """
    m = len(stations)
    t = 0
    stations.append(S)
    prev = 0
    for cur in stations:
        dis = cur - prev
        if dis > V:
            return False
        else:
            t += max(dis * 3 - V, dis)
        if t > T:
            return False
        prev = cur
    return True


def binSearch(S, T, stations):
    """
    to find the least tank volume to enable the aircraft to complete the journey
    the fastest way is to complete the whole journey with the speed of 2km/min, at 2L/km
    V <= 2S 
    """
    l = 0
    r = S * 2
    if T < S:
        return float('inf')
    while l + 1 < r:
        m = l + (r - l) // 2
        if roadToCinema(m, S, T, stations) == True:
            r = m
        else:
            l = m
    return r


def __starting_point():
    line = sys.stdin.readline()
    [N, M, S, T] = list(map(int, line.split(' ')))
    aircrafts = []
    for i in range(N):
        [c, v] = list(map(int, sys.stdin.readline().split(' ')))
        aircrafts.append([c, v])
    stations = list(map(int, sys.stdin.readline().split(' ')))
    stations.sort()
    minVolume = binSearch(S, T, stations)
    if minVolume == float('inf'):
        print(-1)
    else:
        res = float('inf')
        for i in range(N):
            if aircrafts[i][1] >= minVolume:
                res = min(res, aircrafts[i][0])
        if res == float('inf'):
            print(-1)
        else:
            print(res)


__starting_point()

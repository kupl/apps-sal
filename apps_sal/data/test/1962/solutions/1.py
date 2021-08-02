import bisect;


def getIntList():
    return list(map(int, input().split()));


def getTransIntList(n):
    first = getIntList();
    m = len(first);
    result = [[0] * n for _ in range(m)];
    for i in range(m):
        result[i][0] = first[i];
    for j in range(1, n):
        curr = getIntList();
        for i in range(m):
            result[i][j] = curr[i];
    return result;


n, k, l = getIntList();
m = n * k;
a = getIntList();
a.sort();
lowLim = a[0];
upLim = lowLim + l;
# print(a);


def solve():
    if a[n - 1] > upLim:
        return 0;
    i0 = bisect.bisect_right(a, upLim);
    nbBad = m - i0;
    i0 -= 1;
    value = 0;
    for i in range(n - 1, -1, -1):
        diff = min(nbBad, k - 1);
        rest = k - diff;
        nbBad -= diff;
        value += a[i0 - rest + 1];
        #print(i0-rest+1, a[i0-rest+1])
        i0 -= rest;
    return value;


print(solve());

import bisect
from collections import deque
from sys import stdin
tt = int(stdin.readline())

for loop in range(tt):

    n, k = map(int, stdin.readline().split())
    x = list(map(int, stdin.readline().split()))
    y = list(map(int, stdin.readline().split()))

    x.sort()
    unAB = deque([])
    nmax = 0
    ans = 0

    for i in range(n):

        while len(unAB) > 0 and unAB[0][0] < x[i] - k:
            tx, val = unAB.popleft()
            nmax = max(nmax, val)

        ind = bisect.bisect_right(x, x[i] + k)
        val = ind - i
        ans = max(ans, nmax + val)
        unAB.append((x[i], val))

    print(ans)

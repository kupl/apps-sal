import math
start, finish, time = list(map(int, input().split()))
b = int(input())


def solve():
    firstAvailableSpot = start
    minimumTimeInQueue = 10**12 + 1
    minimum = 23123
    last = 0

    for i in range(len(q)):
        if (q[i] > firstAvailableSpot) and (firstAvailableSpot + time < finish):
            return firstAvailableSpot

        timeInQueue = firstAvailableSpot - q[i]
        firstAvailableSpot += time

        if q[i] != last:
            if timeInQueue + 1 < minimumTimeInQueue:
                minimumTimeInQueue = timeInQueue + 1
                minimum = q[i] - 1
                last = q[i]

        if firstAvailableSpot >= finish or len(q) - 1 == i:
            if firstAvailableSpot + time <= finish:
                return firstAvailableSpot
            return minimum


if b != 0:
    q = list(map(int, input().split()))
    print(solve())
else:
    print(str(start))

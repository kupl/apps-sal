class First:
    def __init__(self, seconds, cost):
        self.seconds = seconds
        self.cost = cost


class Second:
    def __init__(self, numCreated, cost):
        self.numCreated = numCreated
        self.cost = cost


def solve():
    potionCount, firstCount, secondCount = map(int, input().split())
    secondsOne, manaPoints = map(int, input().split())
    first = list()
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    for i in range(firstCount):
        first.append(First(a[i], b[i]))
    first.append(First(secondsOne, 0))
    second = [Second(0, 0)]
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    for i in range(secondCount):
        second.append(Second(a[i], b[i]))
    res = int(1e20)
    for f in first:
        low = 0
        high = len(second) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if f.cost + second[mid].cost > manaPoints:
                high = mid - 1
            else:
                low = mid
        if f.cost + second[low].cost <= manaPoints:
            moar = max(0, potionCount - second[low].numCreated)
            time = moar * f.seconds
            res = min(res, time)
    print(res)


solve()

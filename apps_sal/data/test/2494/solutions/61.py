import heapq


def main():
    k = int(input())
    brdict = {}
    for i in range(1, k):
        if i == k - 1:
            if (10 * (k - 1)) % k == 0:
                brdict[i] = [(0, 0)]
            else:
                brdict[i] = [(0, 1)]
        else:
            if i != (i * 10) % k:
                brdict[i] = [((i * 10) % k, 0)]
            if (i * 10) % k != i + 1:
                brdict[i] = brdict.get(i, []) + [(i + 1, 1)]
    start = 1
    cost = [i for i in range(k)]
    cost[0] = k
    fixed = [False] * k
    fixed[start] = True
    akouho = [(1, start)]
    heapq.heapify(akouho)
    while not all(fixed):
        (fcost, fnode) = heapq.heappop(akouho)
        if fnode == 0:
            break
        fixed[fnode] = True
        for br in brdict[fnode]:
            if not fixed[br[0]]:
                if cost[br[0]] > fcost + br[1]:
                    cost[br[0]] = fcost + br[1]
                    heapq.heappush(akouho, (cost[br[0]], br[0]))
        if akouho == []:
            break
    print(cost[0])


def __starting_point():
    main()


__starting_point()

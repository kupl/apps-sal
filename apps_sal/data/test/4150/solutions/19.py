import heapq


def main():
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    q = []
    for i in range(n):
        heapq.heappush(q, (-a[i], i))
    teams = [0] * n
    nextLeft = [i - 1 for i in range(n)]
    nextRight = [i + 1 for i in range(n)]
    used = [False] * n
    team = 0
    while q:
        (item, pos) = heapq.heappop(q)
        while q and used[pos]:
            (item, pos) = heapq.heappop(q)
        if used[pos]:
            break
        teams[pos] = team + 1
        used[pos] = True
        deletedLeft = 0
        currLeft = pos
        while deletedLeft < k and nextLeft[currLeft] >= 0:
            currLeft = nextLeft[currLeft]
            used[currLeft] = True
            teams[currLeft] = team + 1
            deletedLeft += 1
        deletedRight = 0
        currRight = pos
        while deletedRight < k and nextRight[currRight] < n:
            currRight = nextRight[currRight]
            used[currRight] = True
            teams[currRight] = team + 1
            deletedRight += 1
        if currLeft >= 0:
            currLeft = nextLeft[currLeft]
        if currRight < n:
            currRight = nextRight[currRight]
        if currLeft >= 0:
            nextRight[currLeft] = currRight
        if currRight < n:
            nextLeft[currRight] = currLeft
        team = (team + 1) % 2
    print(''.join(map(str, teams)))


def __starting_point():
    main()


__starting_point()

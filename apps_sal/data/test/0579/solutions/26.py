import itertools


def __starting_point():

    N, K = list(map(int, input().split()))
    P = [int(p) - 1 for p in input().split()]
    C = list(map(int, input().split()))

    cycleIDs = [-1 for _ in range(N)]
    cycleInfs = []
    cycleID = 0
    procCnt = 0

    for n in range(N):
        v = n

        if cycleIDs[v] != -1:
            continue
        else:
            currentCycleCosts = []
            while True:
                currentCycleCosts.append(C[v])
                cycleIDs[v] = cycleID

                v = P[v]
                if cycleIDs[v] != -1:
                    procCnt = K % len(currentCycleCosts)
                    if len(currentCycleCosts) + procCnt <= K:
                        procCnt += len(currentCycleCosts)

                    cycleInfs.append((procCnt, len(currentCycleCosts), currentCycleCosts * 3))
                    cycleID += 1
                    break

    ans = -10 ** 9
    for procCnt, currentCycleSize, currentCycleCosts in cycleInfs:

        loopScore = 0
        if sum(currentCycleCosts) > 0:
            cycleLoopCnt = (K - procCnt) // currentCycleSize
            loopScore = cycleLoopCnt * sum(currentCycleCosts[:currentCycleSize])

        for i in range(currentCycleSize):
            ans = max(ans, max(list(itertools.accumulate(currentCycleCosts[i:i + procCnt]))) + loopScore)

    print(ans)


__starting_point()

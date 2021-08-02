m, n, k, t = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
A.sort()
traps = []
for i in range(k):
    l, r, d = [int(s) for s in input().split()]
    traps.append((l, r, d))
traps.sort()


def canTake(agi):
    farest = 0
    trapIndex = 0
    wasteTime = 0
    while trapIndex < len(traps):
        trap = traps[trapIndex]
        if trap[2] <= agi:
            trapIndex += 1
            continue
        if trap[1] <= farest:
            trapIndex += 1
            continue
        # r > farest
        newFarest = trap[1]
        if trap[0] > farest:
            wasteTime += (trap[1] - trap[0] + 1) * 2
        else:
            wasteTime += (newFarest - farest) * 2
        farest = newFarest
        trapIndex += 1

    if wasteTime + n + 1 > t:
        return False
    else:
        return True


def binSearch(A):
    if canTake(A[0]):
        return 0
    low = 0  # imposs tank
    high = len(A)  # poss tank
    while high - low > 1:
        mid = (low + high) // 2
        if canTake(A[mid]):
            high = mid
        else:
            low = mid
    return high


firstCan = binSearch(A)
print(len(A) - firstCan)

def solve():
    strInput = input()
    n = int(strInput)
    strInput = input()
    times = strInput.split()
    totalSolvingTime = 0
    for s in times:
        totalSolvingTime += int(s)
    strInput = input()
    m = int(strInput)
    for i in range(m):
        fullRange = input()
        boundaries = fullRange.split()
        if totalSolvingTime > int(boundaries[1]):
            continue
        else:
            left = int(boundaries[0])
            if left >= totalSolvingTime:
                return left
            else:
                return totalSolvingTime
    return -1


print(solve())

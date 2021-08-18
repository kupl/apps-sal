import math
n, x, m = list(map(int, input().split()))

appearance = {}
sequence = []
a = x
loopExists = False

for _ in range(n):
    appearance[a] = appearance.get(a, 0) + 1
    if appearance[a] == 2:
        loopExists = True
        break
    sequence.append(a)
    a = a * a % m

if not loopExists:
    print((sum(sequence)))
else:
    loopStartIndex = sequence.index(a)
    preLoopNums = sequence[:loopStartIndex]
    loopNums = sequence[loopStartIndex:]
    preLoopLength = len(preLoopNums)
    loopLength = len(loopNums)
    loopCount = (n - preLoopLength) // loopLength
    restLength = (n - preLoopLength) % loopLength
    preLoopTotal = sum(preLoopNums)
    loopTotal = sum(loopNums)
    restTotal = sum(loopNums[:restLength])
    total = preLoopTotal + loopTotal * loopCount + restTotal
    print(total)

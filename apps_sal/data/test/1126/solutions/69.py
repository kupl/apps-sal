# -*- coding: utf-8 -*-
import math
n, x, m = list(map(int, input().split()))

appearance = {}
sequence = []
a = x
loopExists = False

# find loop in numerical sequence. loop length < m
# because m << n, for loop should break sooner than n
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
    # n = preLoopLength + loopCount * loopLength + rest
    loopCount = (n - preLoopLength) // loopLength
    restLength = (n - preLoopLength) % loopLength
    # total = preLoopTotal + loopTotal * loopCount + restTotal
    preLoopTotal = sum(preLoopNums)
    loopTotal = sum(loopNums)
    restTotal = sum(loopNums[:restLength])
    total = preLoopTotal + loopTotal * loopCount + restTotal
    print(total)

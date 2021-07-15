import sys

value = input()
if (len(value) < 7):
    print(0)
    return

res = set()
possible = {}
possible[len(value)] = set([2])
if (len(value) > 7):
    possible[len(value)].add(3)
possibleLen = [2, 3]

for i in reversed(range(7, len(value) + 1)):
    possibleVal = possible.get(i, set())
    for length in possibleVal:
        nextI = i - length
        val = value[nextI:i]
        res.add(val)
        for posLen in possibleLen:
            if (nextI >= 5 + posLen and value[nextI - posLen:nextI] != val):
                setNextI = possible.setdefault(nextI, set())
                setNextI.add(posLen)

print(len(res))
for val in sorted(res):
    print(val)

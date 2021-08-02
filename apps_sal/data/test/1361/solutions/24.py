import sys
numberofrocks = int(sys.stdin.readline())
listofrocks = list(map(int, sys.stdin.readline().rstrip('\n').split()))
listofgaps = [listofrocks[1] - listofrocks[0]]
listofgapsafterremoving = []
for index in range(1, numberofrocks - 1):
    listofgaps.append(listofrocks[index + 1] - listofrocks[index])
    listofgapsafterremoving.append(listofrocks[index + 1] - listofrocks[index - 1])
solution = max(max(listofgaps), min(listofgapsafterremoving))
print(solution)

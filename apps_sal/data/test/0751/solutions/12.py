import sys
3


n, m = [int(nbr) for nbr in sys.stdin.readline().split()]
groups = [int(nbr) for nbr in sys.stdin.readline().split()]

currentBusFilling = 0
nbrOfBusses = 0
for group in groups:
    if group + currentBusFilling < m:
        currentBusFilling += group
    elif group + currentBusFilling != m:
        nbrOfBusses += 1
        currentBusFilling = group
    else:
        nbrOfBusses += 1
        currentBusFilling = 0

if (currentBusFilling == 0):
    print(nbrOfBusses)
else:
    print(nbrOfBusses + 1)

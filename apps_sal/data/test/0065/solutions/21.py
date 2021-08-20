import sys
taille = int(sys.stdin.readline())
tableau = list(map(int, sys.stdin.readline().split()))
mini = min(tableau)
pre = -1
minDist = 10 ** 7
for loop in range(taille):
    if tableau[loop] == mini:
        if pre == -1:
            pre = loop
        else:
            minDist = min(loop - pre, minDist)
            pre = loop
print(minDist)

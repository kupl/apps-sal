import sys
sys.setrecursionlimit(10**8)

k = int(sys.stdin.readline())
liste = list(map(int, sys.stdin.readline().split()))
out = list()
nb = 1
i = 1
for loop in range(1, k):
    if liste[loop] <= liste[loop - 1]:
        nb += 1
        out.append(i)
        i = 1
    else:
        i += 1
out.append(i)
print(nb)
print(*out)

import sys

n = int(sys.stdin.readline())
liste = list(map(int, sys.stdin.readline().split()))
nb = 0
tab = [False] * 601
for loop in range(n):
    if not tab[liste[loop]] and liste[loop] != 0:
        nb += 1
        tab[liste[loop]] = True
print(nb)

'''input
15
4 8 4 8 15 16 8 16 23 15 16 4 42 23 42
'''
# its just a simulation
from sys import stdin, setrecursionlimit
import heapq


def refine(arr):
    aux = []
    for i in range(len(arr)):
        if arr[i] in [4, 8, 15, 16, 23, 42]:
            aux.append(arr[i])
    return aux


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr = refine(arr)
mydict = dict()
mydict[4] = 0
mydict[8] = 0
mydict[15] = 0
mydict[16] = 0
mydict[23] = 0
mydict[42] = 0

for i in range(len(arr)):
    if arr[i] == 4:
        mydict[4] += 1
    elif arr[i] == 8:
        if mydict[4] >= mydict[8] + 1:
            mydict[8] += 1
    elif arr[i] == 15:
        if mydict[8] >= mydict[15] + 1:
            mydict[15] += 1

    elif arr[i] == 16:
        if mydict[15] >= mydict[16] + 1:
            mydict[16] += 1
    elif arr[i] == 23:
        if mydict[16] >= mydict[23] + 1:
            mydict[23] += 1
    elif arr[i] == 42:
        if mydict[23] >= mydict[42] + 1:
            mydict[42] += 1

print(n - mydict[42] * 6)

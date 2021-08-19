import sys
import queue

#file = open("in.txt", "r")
#sys.stdin = file

line = sys.stdin.readline()

n = int(line)

first = ["" for x in range(n)]
second = ["" for x in range(n)]

for i in range(0, n):
    line = sys.stdin.readline().split()
    first[i] = line[0]
    second[i] = line[1]

permutation = [int(x) for x in sys.stdin.readline().split()]

p = permutation[0] - 1
last = min(first[p], second[p])


can = True

for i in range(1, n):
    p = permutation[i] - 1
    if last < min(first[p], second[p]):
        last = min(first[p], second[p])
    elif last < max(first[p], second[p]):
        last = max(first[p], second[p])
    else:
        can = False

if can:
    print("YES")
else:
    print("NO")

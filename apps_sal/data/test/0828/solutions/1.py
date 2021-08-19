""" This is a solution to the problem Subordinates on codeforces.com
    
    There is a DAG with n nodes, pointing towards the root, without further constraints. 
    Given: for each node, a number signifying the count of (direct and indirect) predecessors, and the ID of root s.
    Some of these counts might be wrong. Give the minimum amount of wrong counts.
    
    For details, see
    http://codeforces.com/problemset/problem/729/E
"""

# Idea: count = level of DAG. Check constraints: root has 0 predecessors, level 0 has only one count, each level to the last has be > 0

from sys import stdin

#lines = open("input.txt", 'r').readlines()
lines = stdin.readlines()

n, s = map(int, lines[0].split())
counts = list(map(int, lines[1].split()))

totalwrong = 0
if counts[s - 1] > 0:  # root has to be 0
    totalwrong += 1
    counts[s - 1] = 0

maxlevel = max(counts)
# count number of nodes on levels
levelcount = [0] * (max(counts) + 1)

for c in counts:
    levelcount[c] += 1

curwrong = levelcount[0] - 1  # only one root
levelcount[0] = 1
totalwrong += curwrong

curlevel = 0
while curlevel <= maxlevel:
    lc = levelcount[curlevel]
    if lc == 0:         # a mistake
        if curwrong > 0:  # still mistakes available, just use them to fill
            curwrong -= 1
            levelcount[curlevel] = 1
        else:  # else fill from last level
            levelcount[maxlevel] -= 1
            levelcount[curlevel] = 1
            totalwrong += 1
            while levelcount[maxlevel] == 0:
                maxlevel -= 1       # as levelcount[curlevel] = 1, this aborts at some point
    curlevel += 1
print(totalwrong)

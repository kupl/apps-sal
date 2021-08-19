"""
Created on Mon Jan  8 10:20:50 2018

@author: yanni
"""
(n, T) = [int(x) for x in input().split()]
prob = []
vals = [set() for stuff in range(n + 2)]
for i in range(n):
    (a, t) = [int(x) for x in input().split()]
    prob.append((i + 1, a, t))
prob.sort(key=lambda tup: tup[2])
currindex = 0
maxindex = -1
solve = set()
mem = set()
timeleft = T
target = 1
for currindex in range(n):
    (i, a, t) = prob[currindex]
    if timeleft < t:
        break
    if timeleft >= t and a >= target:
        vals[a].add(currindex)
        solve.add(currindex)
        timeleft -= t
        if len(solve) == target:
            maxindex = currindex
            for p in vals[target]:
                solve.remove(p)
                timeleft += prob[p][2]
            target += 1
bestsolve = solve | vals[target - 1]
solvelist = [x for x in bestsolve if x <= maxindex]
target = len(solvelist)
print(target)
print(target)
for p in solvelist:
    print(prob[p][0], end=' ')
print()

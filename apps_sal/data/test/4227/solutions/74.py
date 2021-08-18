import sys
import itertools

load = []
for i, row in enumerate(sys.stdin.readlines()):
    if i == 0:
        n, m = [int(x) for x in row.split()]
    else:
        load.append({int(x) for x in row.split()})

sum = 0
for one_load in itertools.permutations([i for i in range(1, n + 1)]):
    if one_load[0] != 1:
        continue
    else:
        for i, dot in enumerate(one_load):
            if i == 0:
                old_dot = dot
            else:
                if {old_dot, dot} in load:
                    old_dot = dot
                else:
                    break
        else:
            sum += 1
print(sum)

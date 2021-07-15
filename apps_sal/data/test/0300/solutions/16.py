n = int(input())
labs = [ int(a) for a in input().split() ]

labs.sort()

redo = 0
while sum(labs)/len(labs) < 4.5:
    labs[redo] = 5
    redo += 1

print(redo)


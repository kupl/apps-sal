from collections import defaultdict

def serej(bottles):
    #set of bottles that need to be opened

    unopened = defaultdict(set)

    for i, bottle in enumerate(bottles):
        unopened[bottle[0]].add(i+1)

    for i, bottle in enumerate(bottles):
        if bottle[1] in unopened:
            unopened[bottle[1]] = unopened[bottle[1]].intersection({i+1})

    return sum(len(x) for x in list(unopened.values()))

n = int(input())

bottles = []
for _ in range(n):
    bottles.append([int(x) for x in input().split(' ')])

print(serej(bottles))


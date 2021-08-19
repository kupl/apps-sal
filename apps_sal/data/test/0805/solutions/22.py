n = int(input())
(al, ar) = [int(x) for x in input().split()]
alexSpace = {x: True for x in range(al, ar)}
for i in range(1, n):
    (l, r) = [int(x) for x in input().split()]
    for i1 in range(l, r):
        if i1 in alexSpace.keys():
            alexSpace[i1] = False
print(len({x: isFree for (x, isFree) in alexSpace.items() if isFree}))

n, t = [int(x) for x in input().split()]
curr = [t]
fill = 0

while sum(curr) > 0 and len(curr) <= n:
    nex = [0] * (len(curr) + 1)
    for i in range(len(curr)):
        if curr[i] >= 1:
            fill += 1
            flow = curr[i] - 1
            nex[i] += flow / 2
            nex[i + 1] += flow / 2
    curr = nex

print(fill)

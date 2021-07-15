import sys
for line in sys.stdin:
    cost = 0
    c1,c2,c3,c4 = [int(x) for x in line.split()]
    line = next(sys.stdin)
    n, m = [int(x) for x in line.split()]
    line = next(sys.stdin)
    a = [int(x) for x in line.split()]
    line = next(sys.stdin)
    b = [int(x) for x in line.split()]
    cost1 = 0
    for x in a:
        cost1 += min(x * c1, c2)
    cost1 = min(cost1, c3)
    
    cost2 = 0
    for x in b:
        cost2 += min(x * c1, c2)
    cost2 = min(cost2, c3)
    cost = min(c4, cost1 + cost2)
    print(cost)


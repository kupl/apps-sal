t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    best = 1
    for i, x in enumerate(l):
        if x <= i + 1:
            best = i + 2
    print(best)

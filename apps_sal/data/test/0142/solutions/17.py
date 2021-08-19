(n, lt) = (int(x) for x in input().split())
costs = [int(x) for x in input().split()]
c1 = costs[0]
costs = costs[1:]
maincost = lt * c1
mainlen = lt
remcost = 0
currv = 1
for c in costs:
    currv *= 2
    nmainl = lt - lt % currv
    prevc = maincost / mainlen if maincost != 0 else 0
    if prevc > c / currv:
        nremlen = mainlen - nmainl
        remcost += maincost * nremlen // mainlen
        mainlen = nmainl
        maincost = mainlen * c // currv
    if remcost > c:
        remcost = c
print(maincost + remcost)

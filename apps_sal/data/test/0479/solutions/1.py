n, k = [int(s) for s in input().split()]

bills = [int(s) for s in input().split()]
pairs = {}
for bill in bills:
    for i in range(k):
        possible = (i + 1) * bill
        if possible not in pairs or i + 1 < pairs[possible]:
            pairs[possible] = i + 1
q = int(input())

mymax = 100000000000000000
for i in range(q):
    query = int(input())
    minumum = mymax
    for money, nbills in list(pairs.items()):
        if money == query and nbills <= k and nbills < minumum:
            minumum = nbills
        else:
            rest = query - money
            if rest in pairs and nbills + pairs[rest] < minumum and nbills + pairs[rest] <= k:
                minumum = nbills + pairs[rest]
    if minumum == mymax:
        print(-1)
    else:
        print(minumum)

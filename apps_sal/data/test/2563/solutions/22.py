import sys
INF = 10 ** 9
sys.setrecursionlimit(10 ** 8)
n = int(input())
for i in range(n):
    s = input().rstrip()
    odds = []
    evens = []
    for ch in s:
        if int(ch) % 2 == 0:
            evens.append(int(ch))
        else:
            odds.append(int(ch))
    evens.append(INF)
    odds.append(INF)
    ans = []
    eid = 0
    oid = 0
    while evens[eid] != INF or odds[oid] != INF:
        if evens[eid] < odds[oid]:
            ans.append(evens[eid])
            eid += 1
        else:
            ans.append(odds[oid])
            oid += 1
    print(''.join([str(item) for item in ans]))

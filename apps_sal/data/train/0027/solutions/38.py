a = int(input())
for i in range(a):
    f = int(input())
    k = list(map(int, input().split()))
    l = set()
    ch = 0
    lol = 0
    for i in range(len(k)):
        lol = k[i]
        while lol % 2 == 0:
            l.add(lol)
            lol /= 2
    print(len(l))

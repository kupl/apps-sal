q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if k == 1:
        if max(l) == min(l):
            print(len(l))
            print(*l)
        else:
            print(-1)
    else:
        cyk = set()
        for i in l:
            cyk.add(i)
        if len(cyk) > k:
            dasie = 0
        else:
            dasie = 1
        if dasie == 0:
            print(-1)
        else:
            a = list(cyk)
            while len(a) != k:
                a.append(l[0])
            odp = n * a
            print(len(odp))
            print(*odp)

debug = 0
t = int(input())

for _ in range(t):
    n = int(input())
    ev = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        ev.append((a, -1, i))
        ev.append((b, 1, i))

    ev.sort()
    a = set()
    count = [0] * n
    brks = 0
    are_non_solo = 0
    if debug: print (ev)
    for j in range(2 * n):
        t, d, i = ev[j]
        if debug: print(a,ev[j])
        if d == -1:
            if a:
                are_non_solo=1
            a.add(i)
        else:
            a.remove(i)
            if j +1 < 2 * n and ev[j+1][0] != t:
                if len(a) == 1 and ev[j+1][1] == -1:
                    if debug: print ('ą')
                    for nn in a:
                        count[nn] += 1
                if len(a) == 0:
                    brks += 1

    print(max(count) + brks+are_non_solo)


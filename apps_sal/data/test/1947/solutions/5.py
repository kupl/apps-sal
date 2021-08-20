import sys
(nbmeches, nbreq, l) = list(map(int, sys.stdin.readline().split()))
meches = list(map(int, sys.stdin.readline().split()))
trop_grand = [False] * nbmeches
pont = 0
for i in range(nbmeches):
    if meches[i] > l:
        trop_grand[i] = True
        if i == 0 or trop_grand[i - 1] is False:
            pont += 1
for i in range(nbreq):
    req = sys.stdin.readline().split()
    if int(req[0]) == 0:
        print(pont)
    else:
        meches[int(req[1]) - 1] += int(req[2])
        if meches[int(req[1]) - 1] > l and (not trop_grand[int(req[1]) - 1]):
            trop_grand[int(req[1]) - 1] = True
            if nbmeches == 1:
                pont = 1
            elif int(req[1]) - 1 == 0 and (not trop_grand[int(req[1])]):
                pont += 1
            elif not int(req[1]) - 1 == 0 and int(req[1]) - 1 == nbmeches - 1 and (not trop_grand[int(req[1]) - 2]):
                pont += 1
            elif not int(req[1]) - 1 == 0 and (not int(req[1]) - 1 == nbmeches - 1) and trop_grand[int(req[1])] and trop_grand[int(req[1]) - 2]:
                pont = max(0, pont - 1)
            elif not int(req[1]) - 1 == 0 and (not int(req[1]) - 1 == nbmeches - 1) and (not trop_grand[int(req[1])]) and (not trop_grand[int(req[1]) - 2]):
                pont += 1

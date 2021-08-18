n, K = list(map(int, input().split(" ")))
azaza = {}
all = set()

for i in range(n):
    a, b = list(map(int, input().split(" ")))

    if a not in azaza:
        azaza[a] = []
    if b not in azaza:
        azaza[b] = []

    azaza[a].append(b)
    azaza[b].append(a)

    all.add(a)
    all.add(b)

ans = {}
for i in all:
    ans[i] = []

for i in all:
    for j in all:
        if i != j and j not in azaza[i]:
            lolka = 0
            for k in azaza[i]:
                if j in azaza[k]:
                    lolka = lolka + 1

            if 100 * lolka / len(azaza[i]) >= K:
                ans[i].append(j)

for i in sorted(ans):
    ansstr = str(i) + ": " + str(len(ans[i])) + ' '
    for j in sorted(ans[i]):
        ansstr += str(j) + ' '
    print(ansstr)

def sol():
    n, s = list(map(int, input().split()))
    pref = list(map(int, input().split()))
    mx = [pref[0]]
    ind = [0]
    for j in range(1, n):
        if pref[j] > mx[-1]:
            ind.append(j)
        else:
            ind.append(ind[-1])
        mx.append(max(mx[-1], pref[j]))
        pref[j] += pref[j - 1]
    jnd = 0
    for j in range(n):
        if pref[j] <= s:
            jnd = 0
        elif pref[j] - mx[j] <= s:
            jnd = ind[j] + 1
    print(jnd)


for i in range(int(input())):
    sol()

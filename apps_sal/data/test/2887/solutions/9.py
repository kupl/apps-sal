n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in range(len(t)):
    vap = 0
    for j in range(0, i + 1):
        if v[j] <= 0:
            continue
        if v[j] - t[i] <= 0:
            vap += v[j]
            v[j] = 0
        else:
            vap += t[i]
            v[j] -= t[i]
    print(vap, end=' ')

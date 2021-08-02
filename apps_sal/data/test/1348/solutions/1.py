n, k = list(map(int, input().split()))
d = list(map(int, input().split()))

dmax = max(d)

nv = [[] for i in range(dmax + 1)]
v = [0] * (dmax + 1)

for i, dist in enumerate(d):
    nv[dist].append(i)
    v[dist] += 1

flag = True
if v[0] != 1 or v[1] > k:
    flag = False
else:
    for i in range(2, dmax + 1):
        if v[i] > (k - 1) * v[i - 1] or v[i] == 0:
            flag = False
            break

if flag:
    print(n - 1)
    for vrtx in nv[1]:
        print(nv[0][0] + 1, vrtx + 1)
    for i, vs in enumerate(nv[1:-1]):
        for j, vrtx in enumerate(vs):
            m = 0
            while m < (k - 1):
                if (j * (k - 1) + m) < len(nv[i + 2]):
                    print(vrtx + 1, nv[i + 2][j * (k - 1) + m] + 1)
                    m += 1
                else:
                    break

else:
    print(-1)

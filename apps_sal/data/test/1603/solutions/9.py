count = int(input())
v = [int(c) for c in input().split()]
vsort = v[:]
vsort.sort()
sumV = [0, v[0]]
sumVS = [0, vsort[0]]
for i in range(1, count):
    sumV.append(sumV[i] + v[i])
    sumVS.append(sumVS[i] + vsort[i])

qc = int(input())

for x in range(qc):
    q = [int(c) for c in input().split()]
    if q[0] == 1:
        tmp = sumV
    else:
        tmp = sumVS
    print(tmp[q[2]] - tmp[q[1] - 1])

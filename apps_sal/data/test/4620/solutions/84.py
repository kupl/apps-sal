n = int(input())
csf = [tuple(map(int, input().split())) for _ in range(n - 1)]

arrtime = lambda i, cs: max(csf[i][2] * (cs // csf[i][2] + (cs % csf[i][2] > 0)), csf[i][1]) + csf[i][0]
for i in range(n - 1):
    arrivN = csf[i][1]
    for j in range(i, n - 1):
        arrivN = arrtime(j, arrivN)
    print(arrivN)
print(0)

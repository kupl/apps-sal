import bisect
K = int(input())
D = {}
for i in range(1, 10**4):
    for j in range(12):
        Sunuke = str(i) + ("9" * j)
        if len(Sunuke) <= 15 and Sunuke not in D:
            S = 0
            for k in range(len(Sunuke)):
                S += int(Sunuke[k])
            D[int(Sunuke)] = S
D = list(D.items())
D.sort()
# print(D[:10])

d = [10**16 for i in range(len(D))]
d[0] = 0
ans = [0 for i in range(len(D))]
for i in range(len(D)):
    ans[bisect.bisect_right(d, D[i][0] / D[i][1])] = D[i][0]
    d[bisect.bisect_right(d, D[i][0] / D[i][1])] = D[i][0] / D[i][1]

# print(ans[:50])
ANS = []
MAX = 0
for i in range(len(ans)):
    if ans[i] > MAX:
        ANS.append(ans[i])
        MAX = ans[i]
# print(ANS[:100])
for i in range(K):
    print((ANS[i]))
# print(d[:10])

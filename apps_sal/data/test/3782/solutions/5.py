import sys
input = sys.stdin.readline
(N, K, Q) = list(map(int, input().split()))
a = list(map(int, input().split()))
ta = a + []
res = pow(10, 10)
bs = pow(10, 10)
for x in sorted(set(a)):
    t = [[]]
    for i in range(N):
        if ta[i] == bs:
            if t[-1] != []:
                t.append([])
        else:
            t[-1].append(a[i])
    tt = []
    for i in range(len(t)):
        t[i].sort()
        for j in range(len(t[i]) - K + 1):
            tt.append(t[i][j])
    if len(tt) < Q:
        break
    tt.sort()
    res = min(res, tt[Q - 1] - tt[0])
    for i in range(N):
        if a[i] == x:
            ta[i] = bs
print(res)

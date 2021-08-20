(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
segments = []
for i in range(m):
    (l, r) = list(map(int, input().split()))
    segments.append([l, r])
ans = 0
flag = 0
for i in range(n):
    for j in range(i, n):
        ai = a[i]
        aj = a[j]
        seglist1 = []
        seglist2 = []
        for k in range(m):
            if segments[k][0] - 1 <= i <= segments[k][1] - 1 and segments[k][1] - 1 < j:
                ai -= 1
                seglist1.append(k + 1)
            if segments[k][0] - 1 > i and segments[k][0] - 1 <= j <= segments[k][1] - 1:
                aj -= 1
                seglist2.append(k + 1)
        if ans < a[j] - ai:
            anslist = seglist1
            ans = a[j] - ai
            flag = 1
        if ans < a[i] - aj:
            anslist = seglist2
            ans = a[i] - aj
            flag = 1
if flag == 1 and len(anslist) >= 1:
    ansseg = str(anslist[0])
    for i in range(1, len(anslist)):
        ansseg += ' ' + str(anslist[i])
else:
    anslist = []
    ansseg = ''
print(ans)
print(len(anslist))
print(ansseg)

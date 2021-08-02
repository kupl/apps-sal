from operator import eq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

al = [False for _ in range(n)]
bl = [False for _ in range(n)]

for i in range(n):
    al[a[i] - 1] = True
    bl[b[i] - 1] = True

for i, e in enumerate(al):
    if not e:
        ak = i + 1

for i, e in enumerate(bl):
    if not e:
        bk = i + 1

aa = [(e, i) for (i, e) in enumerate(a)]
bb = [(e, i) for (i, e) in enumerate(b)]

aa.sort();
bb.sort();


for i in range(1, n):

    if (aa[i][0] == aa[i - 1][0]):
        amis = aa[i][0]
        a1 = aa[i - 1][1]
        a2 = aa[i][1]

    if (bb[i][0] == bb[i - 1][0]):
        bmis = bb[i][0]
        b1 = bb[i - 1][1]
        b2 = bb[i][1]


for ay in [a1, a2]:
    for by in [b1, b2]:
        reta = list(a)
        reta[ay] = ak

        retb = list(b)
        retb[by] = bk

        if all(map(eq, reta, retb)):
            print(" ".join(map(str, reta)))
            return

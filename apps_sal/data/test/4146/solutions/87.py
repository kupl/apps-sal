import collections
N = int(input())
*V, = map(int, input().split())


c1 = collections.Counter(V[0::2])
c1 = sorted(c1.items(), key=lambda x: x[1], reverse=True)
e = c1[0][0]

c2 = collections.Counter(V[1::2])
c2 = sorted(c2.items(), key=lambda x: x[1], reverse=True)
o = c2[0][0]

cnt = 0
if e != o:
    cnt = sum(e != i for i in V[0::2])
    cnt += sum(o != i for i in V[1::2])
else:
    if len(c1) == 1 and len(c2) == 1:
        cnt = N // 2
    elif len(c1) == 1:
        cnt1 = sum(e != i for i in V[0::2])
        cnt1 += sum(c2[1][0] != i for i in V[1::2])

        cnt2 = sum(e != i for i in V[0::2])
        cnt2 += sum(c2[1][1] != i for i in V[1::2])
        cnt = min(cnt1, cnt2)
    elif len(c2) == 1:
        cnt1 = sum(c1[1][0] != i for i in V[0::2])
        cnt1 += sum(o != i for i in V[1::2])

        cnt2 = sum(c1[1][1] != i for i in V[0::2])
        cnt2 += sum(o != i for i in V[1::2])
        cnt = min(cnt1, cnt2)
    else:
        cnt1 = sum(e != i for i in V[0::2])
        cnt1 += sum(c2[1][0] != i for i in V[1::2])

        cnt2 = sum(c1[1][0] != i for i in V[0::2])
        cnt2 += sum(o != i for i in V[1::2])
        cnt = min(cnt1, cnt2)
print(cnt)

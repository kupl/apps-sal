r = lambda: int(input())
ra = lambda: [*list(map(int, input().split()))]
a = []
t, q, mq, s = 0, 0, 0, 0
n = r()
for i in range(n):
    a.append(ra())
for i in range(n):
    if i==0:
        q = a[i][1]
        t = a[i][0]
    else:
        s = a[i][0] - t
        q-=s
        if q<0:
            q = 0
        q+=a[i][1]
    if q>mq:
        mq = q
    t = a[i][0]
t = a[i][0]+q
print(t, mq)


import bisect

t = int(input())

q = []
ans = [float("inf")] * t
ansabc = [[0] * 3 for i in range(t) ]

for loop in range(t):

    a,b,c = map(int,input().split())
    q.append([a,b,c])

for nb in range(1,30001):

    mlis = []
    now = 1

    while now ** 2 <= nb:
        if now ** 2 == nb:
            mlis.append(now)
            break
        elif nb % now == 0:
            mlis.append(now)
            mlis.append(nb // now)

        now += 1

    mlis.sort()
    mlis.append(float("inf"))

    for i in range(t):

        a,b,c = q[i]

        nans = abs(b-nb)

        if c < nb:
            nans += nb-c
            ansc = nb
        else:

            if c % nb < nb - c%nb:
                ansc = c // nb * nb
            else:
                ansc = c // nb * nb + nb
            nans += min(c % nb , nb - c%nb)

        ind = bisect.bisect_left(mlis,a)

        if abs(a - mlis[ind]) < abs(a - mlis[ind-1]):
            ansa = mlis[ind]
        else:
            ansa = mlis[ind-1]
        nans += min(abs(a - mlis[ind]) , abs(a - mlis[ind-1]))

        if ans[i] > nans:
            ans[i] = nans
            ansabc[i] = [ansa,nb,ansc]

for i in range(t):
    print (ans[i])
    print (" ".join(map(str,ansabc[i])))

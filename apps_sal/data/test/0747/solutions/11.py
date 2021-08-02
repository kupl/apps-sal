from copy import deepcopy


def getBetter(h, a):
    maxi = -1
    im = -1
    for i in range(len(a)):
        if (h >= a[i][0]):
            if (maxi < a[i][1]):
                im = i
                maxi = a[i][1]
    return(im, maxi)


n, h0 = map(int, input().split())

lolipops0 = [[], []]

for i in range(n):
    t, h, m = map(int, input().split())
    lolipops0[t].append((h, m))

lolipops0[1].sort()
lolipops0[0].sort()

lolipops1 = deepcopy(lolipops0)

lol0 = getBetter(h0, lolipops0[0])
t1 = 0
h1 = h0
lol1 = getBetter(h0, lolipops0[1])
t2 = 1  # ---- WARNING --------
h2 = h0
while(lol0[0] >= 0 or lol1[0] >= 0):
    if (lol0[0] > -1):
        if (len(lolipops0[t1 % 2]) != 1 and lol0[0] != -1):
            lolipops0[t1 % 2].pop(lol0[0])
        else:
            lolipops0[t1 % 2] = []
        t1 += 1
        h1 += lol0[1]
        lol0 = getBetter(h1, lolipops0[t1 % 2])
    if (lol1[0] > -1):
        if (len(lolipops1[t2 % 2]) != 1 and lol1[0] != -1):
            lolipops1[t2 % 2].pop(lol1[0])
        else:
            lolipops1[t2 % 2] = []
        t2 += 1
        h2 += lol1[1]
        lol1 = getBetter(h2, lolipops1[t2 % 2])
print(max(t1, t2 - 1))

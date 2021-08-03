a = input().split(" ")
h = int(a[1])
n = int(a[0])

candies = []
for i in range(n):
    s = input().split(" ")
    candies.append([int(s[0]), int(s[1]), int(s[2])])

zap = []
for i in range(n):
    zap.append(candies[i])


def eat(bl, cand, h):
    ch = h
    color = bl
    for i in range(n):
        maxJ = -1
        maxM = -1
        for j in range(len(cand)):
            if cand[j][0] == color:
                if cand[j][2] >= maxM and ch >= cand[j][1]:
                    maxJ = j
                    maxM = cand[j][2]
        if maxM == -1:
            return i
        else:
            color = 1 - color
            ch += maxM
            cand.remove(cand[maxJ])
    return n


a = eat(1, candies, h)
b = eat(0, zap, h)
if(a > b):
    print(a)
else:
    print(b)

n = int(input())
l = 2 * n
w = [int(i) for i in input().split()]
pas = input()
seat = [i for i in w]
seat.sort()
d = {}
for i in range(len(w)):
    d[w[i]] = i
i = 0
w1 = [0] * l
j = 0
wkend = " "
for k in range(l):
    if k == l - 1:
        wkend = "\n"
    if pas[k] == "0":
        wkindex = d[seat[i]] + 1
        print(wkindex, end=wkend)
        j += 1
        w1[j] = wkindex
        i += 1
    else:
        print(w1[j], end=wkend)
        j -= 1

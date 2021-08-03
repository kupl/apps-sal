n = int(input())
s = input()

r, b = 0, 0
for x in s:
    if(x == 'r'):
        r += 1
    else:
        b += 1

trr = [x for x in s]
if(n):
    krr = trr[:]
    c = 0

    i = 0
    for p in range(0, n, 2):
        if(krr[p] == 'b'):
            i += 1
    j = 0
    for p in range(1, n, 2):
        if(krr[p] == 'r'):
            j += 1

    krr = trr[:]
    lrr = [max(i, j)]
    c = 0

    i = 0
    for p in range(0, n, 2):
        if(krr[p] == 'r'):
            i += 1
    j = 0
    for p in range(1, n, 2):
        if(krr[p] == 'b'):
            j += 1

    lrr.append(max(i, j))
    print(min(lrr))

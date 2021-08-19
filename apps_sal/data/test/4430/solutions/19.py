def bS(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    posi = -1
    while (first <= last + 1) and (not found):
        midpoint = (first + last) // 2
        #print(midpoint,alist[midpoint-1] )
        if (alist[midpoint] >= item):  # and (alist[midpoint+1] <= item):
            found = True
            posi = midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return posi


n, m, k = list(map(int, input().split()))
a = list(input().split())
maxi = 0
cc = 0
now = -1
alr = 0
alfa = [0] * n
last = 0
for ii in range(n):
    i = n - ii - 1
    alfa[ii] = int(a[i]) + last
    last = alfa[ii]

# print(alfa)
if alfa[-1] > m * k:
    pos = bS(alfa, m * k)
else:
    pos = n - 1

# print(pos)
ii = n - pos - 1
# b=a[ii+1:].copy()
b = a
b.reverse()
maxi = 0
start = 0
# for start in range(n):
if (1 == 1):
    # if n-start<maxi:
    #    break
    alr = 0
    cc = 0
    for i in b[start:]:
        alr += int(i)
        cc += 1

        if alr > k:
            alr = int(i)
            if alr > k:
                cc -= 1
            m -= 1
            if m == 0:
                cc -= 1
                break
    if cc > maxi:
        maxi = cc


print(maxi)

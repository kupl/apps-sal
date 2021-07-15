iData = list(map(int, str(input()).split(" ")))
a, k = [x for x in str(iData[0])], iData[1]

res = []
while k > 0 and len(a) > 1:
    imax = a.index(max(a[:k+1]))
    res.append(a[imax])
    a = a[:imax] + a[imax+1:]
    k-=imax

print("".join(res+a))


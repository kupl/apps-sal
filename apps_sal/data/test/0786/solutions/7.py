n = int(input())
minr = -1000000000000000000
maxr = 1000000000000000000
for i in range(n):
    c, div = [int(x) for x in input().split()]
    if div == 1:
        if minr < 1900:
            minr = 1900
    else:
        if maxr >= 1900:
            maxr = 1899
    minr += c
    maxr += c

if minr > maxr:
    print("Impossible")
elif maxr > 10000000000:
    print("Infinity")
else:
    print(maxr)

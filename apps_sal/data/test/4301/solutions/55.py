n = int(input())
a = list((int(input()) for i in range(n)))
aa = sorted(a)
amax = aa[n - 1]
asecond = aa[n - 2]
for i in a:
    if i != amax:
        print(amax)
    else:
        print(asecond)

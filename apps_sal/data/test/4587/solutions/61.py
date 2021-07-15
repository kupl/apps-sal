import bisect
n=int(input())
a = list(map(int, input("").split()))
b = list(map(int, input("").split()))
c = list(map(int, input("").split()))
out=0
a.sort()
b.sort()
c.sort()
for i in b:
    na = bisect.bisect_left(a,i)
    nc = bisect.bisect(c,i)
    out += na * (len(c)-nc)
print(out)

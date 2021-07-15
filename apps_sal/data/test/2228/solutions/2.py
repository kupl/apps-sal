from bisect import bisect_right
n = int(input())
bs = []
ds = []
for i in range(n):
    b, d = map(int, input().split())
    bs.append(b)
    ds.append(d)
bs.sort()
ds.sort()
maxpop = 0
bestyear = 0
for i in range(len(bs)):
    died_at_this_point = bisect_right(ds, bs[i])
    if maxpop < i+1 - died_at_this_point:
        maxpop = i+1 - died_at_this_point
        bestyear = bs[i]
print(bestyear, maxpop)

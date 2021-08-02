from bisect import bisect_right
n = int(input())
a = [-int(input()) for i in range(n)]
l = []
for aa in a:
    idx = bisect_right(l, aa)
    if idx == len(l):
        l.append(aa)
    else:
        l[idx] = aa
print(len(l))

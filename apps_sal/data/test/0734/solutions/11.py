n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = 0
same = 0
p = 1
for h in a:
    if p <= h:
        p += 1
    else:
        same += 1
res = a[-1] + same
print(sum(a) - res)

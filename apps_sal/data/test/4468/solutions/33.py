n, t = map(int, input().split())
l = list(map(int, input().split()))
s = 0
pre_end = 0
for tt in l:
    time = t - max(0, pre_end - tt)
    s += time
    pre_end = tt + t
print(s)

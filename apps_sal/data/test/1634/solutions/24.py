from math import floor
c1, c2, c3, c4 = list(map(int, input().split()))
n, m = list(map(int, input().split()))
# TODO worth doing a test it analysis
bus = [int(x) for x in input().split()]
trol = [int(x) for x in input().split()]


thres = floor(c2/c1)

## calculate bus side
bus_res = 0
for v in bus:
    if v>thres:
        bus_res += c2
    else:
        bus_res += (v * c1)

bus = min(c3, bus_res)


trol_res = 0
for v in trol:
    if v>thres:
        trol_res += c2
    else:
        trol_res += (v * c1)

trol = min(c3, trol_res)

print(min((bus + trol), c4))



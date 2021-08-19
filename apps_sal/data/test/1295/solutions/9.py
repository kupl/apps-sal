import bisect
x = list(map(int, input().split()))
gor = sorted(list(set(map(int, input().split()))))
vysh = sorted(list(set(map(int, input().split()))))
r = 0
for x in gor:
    vh = bisect.bisect_left(vysh, x)
    if vh == len(vysh) or vysh[vh] != x:
        if vh == 0:
            r = max(r, vysh[vh] - x)
        elif vh == len(vysh):
            r = max(r, x - vysh[vh - 1])
        else:
            r = max(r, min(vysh[vh] - x, x - vysh[vh - 1]))
print(r)

trash = int(input())
line1 = [int(x) for x in input().split()]
low = min(line1)
lows = []
for i in range(0, len(line1)):
    if line1[i] == low:
        lows.append(i)
dists = []
for i in range(1, len(lows)):
    dists.append(lows[i] - lows[i - 1] - 1)
dists.append(lows[0] + (len(line1) - 1) - lows[-1])
print(max(dists) + low * len(line1))

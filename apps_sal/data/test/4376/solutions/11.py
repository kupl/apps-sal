from bisect import bisect_left

a, b = list(map(int, input().split()))
flats = list(map(int, input().split()))
lets = list(map(int, input().split()))

nflats = []
s = 0
for x in flats:
    s += x
    nflats.append(s)

for x in lets:
    y = bisect_left(nflats, x)
    if y != 0:
        print(y + 1, x - nflats[y - 1])
    else:
        print(y + 1, x)

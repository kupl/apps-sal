n, s = map(int, input().split())

flats = {}

for i in range(n):
    f, t = map(int, input().split())
    if f not in flats:
        flats[f] = 0
    flats[f] = max(flats[f], t)

curr_time = 0
for i in range(s, -1, -1):
    if i in flats:
        if curr_time < flats[i]:
            curr_time = flats[i]
    curr_time += 1

print(curr_time - 1)

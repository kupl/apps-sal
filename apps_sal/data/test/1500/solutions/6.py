a = input().split()
n, k = int(a[0]), int(a[1])
sharings = []
s = 0
coords = input().split()
for i in range(n):
    coord = int(coords[i])
    sharings.append(coord)
    if i != 0 and sharings[i - 1] + k < coord:
        s = 1
if s != 1:
    c = 1
    j = 1
    i = 0
    while j < n - 1:
        if sharings[i] + k < sharings[j + 1]:
            c += 1
            i = j
        j += 1
    print(c)
else:
    print(-1)

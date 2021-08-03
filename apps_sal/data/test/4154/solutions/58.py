n, m = list(map(int, input().split()))
min = 1
max = n

for i in range(m):
    l, r = list(map(int, input().split()))
    if min < l:
        min = l
    if max > r:
        max = r

if min > max:
    print((0))
else:
    print((max - min + 1))

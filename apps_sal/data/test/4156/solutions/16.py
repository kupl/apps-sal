n, w = list(map(int, input().split()))
a = list(map(int, input().split()))

max_p = 0
min_p = 0

s = 0
for step in a:
    s += step
    if s > max_p:
        max_p = s
    if s < min_p:
        min_p = s

d = max_p - min_p

#print(max_p, min_p, d)

if w - d + 1 > 0:
    print(w - d + 1)
else:
    print(0)


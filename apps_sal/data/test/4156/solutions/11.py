n, w = list(map(int, input().split()))
ar = list(map(int, input().split()))

difs = []
s = 0
for x in range(n):
    s += ar[x]
    difs.append(s)

minn, maxx = min(difs), max(difs)
maxres, minres = w, 0
if maxx > 0:
    maxres -= maxx
if minn < 0:
    minres -= minn

if maxres < 0 or minres > w or minres > maxres:
    print(0)
else:
    print(maxres - minres + 1)

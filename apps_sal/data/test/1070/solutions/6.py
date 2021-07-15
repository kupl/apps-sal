n, k = list(map(int, input().strip().split()))
colors = list(map(int, input().strip().split()))

l = 0
previ = -1
for i in range(n-1):
    if colors[i] == colors[i+1]:
        cl = i - previ
        if cl > l:
            l = cl
        previ = i

if previ == -1:
    l = n
else:
    cl = (n-1) - previ
    if cl > l:
        l = cl

print(l)

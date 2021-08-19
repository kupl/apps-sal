n = input()
ax = list(map(int, input().split()))
c = 0
last = -1
cmax = 0
for a in ax:
    if a >= last:
        c += 1
    else:
        cmax = max(c, cmax)
        c = 1
    last = a
cmax = max(c, cmax)
print(cmax)

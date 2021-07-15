colors = list(input())
colors.sort()
wants = list(input())
wants.sort()

res = 0

hecan = 1
for c in wants:
    if c not in colors:
        hecan = 0

ca = sorted(set(colors))
wa = sorted(set(colors))

for c in ca:
    if colors.count(c) >= wants.count(c):
        res += wants.count(c)
    else:
        res += colors.count(c)
    #print(colors.count(c), wants.count(c))

if hecan == 0:
    print(-1)
else:
    print(res)


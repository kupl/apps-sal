N = int(input())
stuff = []
for n in range(N):
    l = list(map(int, input().split()))
    stuff.append([l[1], l[0]])
stuff.sort()
lp = -1
happy = False
for s in stuff:
    if s[1] < lp:
        happy = True
        break
    lp = s[1]
print('Happy Alex' if happy else 'Poor Alex')

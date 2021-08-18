n, m, k = list(map(int, input().split()))

p = list(map(int, input().split()))
s = list([int(x) - 1 for x in input().split()])
c = list([int(x) - 1 for x in input().split()])

cc = [None] * m

for x in range(0, m):
    who = [y for y in range(0, n) if s[y] == x]
    who.sort(key=lambda y: p[y])
    who.reverse()
    cool = False
    if len(who) >= 2 and p[who[0]] == p[who[1]]:
        cool = True
    if len(who) == 0:
        who = [-1]
    cc[x] = (cool, who[0])


a = 0
for x in c:
    if len([y for y in cc if not y[0] and y[1] == x]) == 0:
        a += 1

print(a)

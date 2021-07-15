n = int(input())
neg = []
pos = []

for i in range(n):
    inp = input().split()
    x = int(inp[0])
    a = int(inp[1])
    if x < 1:
        neg += [[-x, a]]
    else:
        pos += [[x,a]]

neg = sorted(neg)
pos = sorted(pos)
ne = len(neg)
p = len(pos)
num = ne
longer = pos
notsame = True

if ne > p:
    num = p
    longer = neg
elif ne == p:
    notsame = False

a = 0
for i in range(num):
    a += pos[i][1]
    a += neg[i][1]
if notsame:
    a += longer[num][1]

print(a)

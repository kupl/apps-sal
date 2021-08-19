n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l = list(sorted(l))
pos = []
neg = []
for i in range(n):
    if l[i][0] < 0:
        neg.append(l[i][1])
    else:
        pos.append(l[i][1])
neg = list(reversed(neg))
if len(neg) == len(pos):
    print(sum(neg) + sum(pos))
elif len(neg) > len(pos):
    print(sum(pos) + sum(neg[:len(pos) + 1]))
else:
    print(sum(neg) + sum(pos[:len(neg) + 1]))

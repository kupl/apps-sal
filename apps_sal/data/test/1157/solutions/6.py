a = int(input())
l = list(map(int, input().strip().split()))
neg = [0]
pos = [0]
for i in l:
    t = neg[-1]
    v = pos[-1]
    if i < 0:
        pos.append(t)
        neg.append(v + 1)
    else:
        pos.append(v + 1)
        neg.append(t)
n = 0
p = 0
for i in range(len(pos)):
    n += neg[i]
    p += pos[i]
print(n, p)

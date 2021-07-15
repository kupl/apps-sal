n, v = list(map(int,input().split()))
f = list()
for i in range(n):
    f.append(list(map(int,input().split())))
f.sort()
sum = 0
today = 0
tomor = 0
day = 0
rest = 0
for tree in f:
    if tree[0] > day + 1:
        sum += min(tomor, v)
        tomor = tree[1]
        sum += min(tomor, v)
        rest = v - min(tomor, v)
        tomor -= min(tomor,v)
        day = tree[0]
    elif tree[0] == day + 1:
        sum += min(tomor, v)
        rest = v - min(tomor, v)
        tomor = tree[1]
        t = min(tomor, rest)
        sum += t
        rest -= t
        tomor -= t
        day = tree[0]
    else :
        tomor += tree[1]
        t = min(tomor, rest)
        sum += t
        rest -= t
        tomor -= t
sum += min(tomor, v)
print(sum)


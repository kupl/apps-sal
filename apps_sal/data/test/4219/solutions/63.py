

n = int(input())
li = []
for i in range(n):
    a = int(input())
    subli = []
    for j in range(a):
        x, y = list(map(int, input().split()))
        subli.append([x, y])
    li.append(subli)

ans = 0

for i in range(2 ** n):
    tf = [False] * n
    out = False
    for j in range(n):
        if ((i >> j) & 1):
            tf[j] = True
    for k in range(len(li)):
        if (tf[k] == True):
            for l in li[k]:
                if not(l[1] == tf[l[0]-1]):
                    out = True
    if not (out):
        ans = max(ans, tf.count(True))

print(ans)


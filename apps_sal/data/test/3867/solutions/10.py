from collections import defaultdict
n = int(input())
l = defaultdict(list)

for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    l[x].append(y)
    l[y].append(x)

a = [int(i) - 1 for i in input().split(' ')]

vis = [0] * (n + 10)

if(a[0] != 0):
    print('No')
    return
x = 1
for i in range(n):
    s1 = set()
    vis[a[i]] = 1
    for j in l[a[i]]:
        if(not vis[j]):
            s1.add(j)
    s2 = set()
    for j in range(len(s1)):
        s2.add(a[x])
        x += 1
    if(s1 != s2):
        print('No')
        return
print('Yes')

from collections import defaultdict
n,m,h = list(map(int,input().split()))
a = list(map(int,input().split()))  # m items
b = list(map(int,input().split()))  # n items 0<=b<=h


front = defaultdict(int)
for i, x in enumerate(a):
    front[i] = x
left = defaultdict(int)
for i, x in enumerate(b):
    left[i] = x

out = [[0 for x in range(m)] for y in range(n)]
for i in range(n):
    x = list(map(int,input().split())) # m items
    for j, b in enumerate(x):
        if b:
            out[i][j] = min(left[i],front[j])

for x in out:
    print(*x)


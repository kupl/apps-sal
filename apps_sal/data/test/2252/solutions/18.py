(x, y) = list(map(int, input().split()))
t = 0
awan = list(map(int, input().split()))
for v in range(0, y):
    (l, r, x) = list(map(int, input().split()))
    l -= 1
    x -= 1
    t = 0
    for j in range(l, r):
        if awan[x] > awan[j]:
            t += 1
    if l + t == x:
        print('Yes')
    else:
        print('No')

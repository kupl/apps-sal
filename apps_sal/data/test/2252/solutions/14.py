(n, k) = list(map(int, input().split()))
l = input()
z = [int(i) for i in l.split()]
for i in range(k):
    (l, r, x) = list(map(int, input().split()))
    (l, r, x) = (l - 1, r - 1, x - 1)
    y = 0
    t = z[x]
    for j in range(l, r + 1):
        if z[j] < t:
            y += 1
    if l + y == x:
        print('Yes')
    else:
        print('No')

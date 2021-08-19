(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(m):
    (l, r, x) = [int(x) - 1 for x in input().split()]
    for j in range(l, r + 1):
        if a[j] < a[x]:
            l += 1
            if l > x:
                break
    if l == x:
        print('Yes')
    else:
        print('No')

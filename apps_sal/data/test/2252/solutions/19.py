(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(m):
    (l, r, x) = list(map(int, input().split()))
    count_less = 0
    for j in range(l - 1, r):
        if a[j] < a[x - 1]:
            count_less += 1
    new_pos = l + count_less
    if new_pos == x:
        print('Yes')
    else:
        print('No')

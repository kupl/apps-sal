(a, b) = list(map(int, input().split()))
p = list(map(int, input().split()))
for i in range(b):
    (l, r, x) = list(map(int, input().split()))
    l -= 1
    r -= 1
    x -= 1
    ans = 0
    for i in range(l, r + 1):
        if p[i] <= p[x]:
            ans += 1
    if ans == x - l + 1:
        print('Yes')
    else:
        print('No')

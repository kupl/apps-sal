(n, m) = list(map(int, input().split()))
for i in range(m):
    if i == 0:
        (l, r) = list(map(int, input().split()))
    else:
        (l2, r2) = list(map(int, input().split()))
        l = max(l, l2)
        r = min(r, r2)
if l > r:
    print(0)
else:
    print(r - l + 1)

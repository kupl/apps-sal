l1,r1,l2,r2,k = list(map(int, input().split()))

if r1 < l2:
    print(0)
elif r2 < l1:
    print(0)
else:
    l = max(l1, l2)
    r = min(r1, r2)
    if k < l or k > r:
        print(r - l + 1)
    else:
        print(r - l + 1 - 1)


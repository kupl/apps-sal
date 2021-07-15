l1, r1, l2, r2, k = list(map(int, input().split()))
if l1 >= l2 and r1 <= r2:
    if l1 <= k and r1 >= k:
        print(r1 - l1)
    else:
        print(r1 - l1 + 1)
elif l2 >= l1 and r2 <= r1:
    if l2 <= k and r2 >= k:
        print(r2 - l2)
    else:
        print(r2 - l2 + 1)
elif l1 <= l2 and l2 <= r1 and r1 <= r2:
    if l2 <= k and r1 >= k:
        print(r1 - l2)
    else:
        print(r1 - l2 + 1)
elif l2 <= l1 and l1 <= r2 and r2 <= r1:
    if l1 <= k and r2 >= k:
        print(r2 - l1)
    else:
        print(r2 - l1 + 1)
else:
    print(0)


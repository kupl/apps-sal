l1, r1, l2, r2, k = list(map(int, input().split()))

a = b = -1
if l1 <= l2 and r2 <= r1:
    a, b = l2, r2
elif l2 <= l1 and r1 <= r2:
    a, b = l1, r1
elif l1 <= l2 <= r1:
    a, b = l2, r1
elif l1 <= r2 <= r1:
    a, b = l1, r2

if a == -1 or b == -1:
    print(0)
else:
    res = b - a + 1
    if a <= k <= b:
        res -= 1
    print(res)


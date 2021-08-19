t = int(input())
for _ in range(t):
    valid = True
    n = int(input())
    ar = [int(x) for x in input().split()]
    ar = sorted(ar)
    res = []
    ar1 = ar[:n // 2]
    ar2 = ar[n // 2:][::-1]
    for (a, b) in zip(ar1, ar2):
        res.append(a)
        res.append(b)
    if len(ar2) > len(ar1):
        res.append(ar2[-1])
    for v in res[::-1]:
        print(v, end=' ')
    print()

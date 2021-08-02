n = int(input())
succ = False;
for ii in range(0, 100):
    i = 2 ** ii
    l = 1
    r = 2 ** 100
    while l < r:
        mid = (l + r) // 2
        x = 2 * mid - 1
        v = x * ((x - 1) // 2 + i - 1)
        if v == n:
            succ = True
            print(x * i)
            break
        elif v < n:
            l = mid + 1
        else:
            r = mid
if not succ:
    print("-1")

q = int(input())
for qq in range(q):
    n = int(input())
    *a, = list(map(int, input().split()))
    a = list(sorted(a))
    br = False
    for i in range(2 * n):
        if a[2 * i] != a[2 * i + 1]:
            print("NO")
            br = True
            break
    if br:
        continue
    a = a[::2]
    ar = a[0] * a[-1]
    for i in range(n):
        if a[i] * a[-i - 1] != ar:
            print("NO")
            break
    else:
        print("YES")

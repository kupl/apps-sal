q = int(input())
while q:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    d = False
    while i < len(a) - 1:
        if 2048 in a:
            d = True
            break
        if a[i] == a[i + 1]:
            a.append(a[i] + a[i + 1])
            a.sort()
            i += 2
        else:
            i += 1
    if 2048 in a:
        d = True
    if d:
        print("YES")
    else:
        print("NO")
    q -= 1

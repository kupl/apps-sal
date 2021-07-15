n, m, k = [int(x) for x in input().split(' ')]
a = [int(x) for x in input(' ').split(' ')]
a.sort(reverse=True)

if m <= k:
    print(0)
else:
    u = 0
    for r in a:
        u += 1
        k += r - 1
        if m <= k:
            break
    if m <= k:
        print(u)
    else:
        print(-1)

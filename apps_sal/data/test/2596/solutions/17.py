n, k, m, t = input().split()
n, k, m, t = int(n), int(k), int(m), int(t)

for i in range(t):
    what, pos = input().split()
    what, pos = int(what), int(pos)
    if what == 0:
        if pos >= k:
            n = pos
        else:
            n = n-pos
            k = k-pos
    else:
        n += 1
        if pos <= k:
            k += 1
    print(n, end=" ")
    print(k)




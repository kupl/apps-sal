a = int(input())
for i in range(a):
    b = int(input())
    l = list(map(int, input().split()))
    k = []
    t = [i for i in range(b + 1)]
    k.append(l[0])
    last = k[0]
    j = 0
    t[last] = 0
    for i in l[1:]:
        if i != last:
            last = i
            k.append(last)
            t[last] = 0
        else:
            while t[j] == 0:
                j += 1
            k.append(t[j])
            j += 1
    ch = [k[0]]
    for i in k[1:]:
        ch.append(max(ch[-1], i))
    if l != ch:
        print(-1)
    else:
        print(*k)

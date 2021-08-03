q = int(input())
for _ in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    zlep = 0
    zlen = 0
    for i in range(n):
        if i % 2 == 0:
            zlep += (i - l[i]) % 2
        else:
            zlen += (i - l[i]) % 2
    if zlen == zlep:
        print(zlen)
    else:
        print(-1)

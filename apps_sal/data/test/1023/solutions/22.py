from bisect import bisect_left as br
n, m, ta, tb, k = map(int, input().split())
a = [int(e) + ta for e in input().split()]
b = [int(e) for e in input().split()]
if(k >= min(m, n)):
    print(-1)
else:
    a.sort()
    b.sort()
    # print(*a)
    # print(*b)
    f, mx = 0, -1
    for i in range(0, k + 1):
        x = br(b, a[i])
        if(x + k - i >= m):
            f = 1
        else:
            mx = max(mx, b[x + k - i])
    if(f == 1):
        print(-1)
    else:
        print(mx + tb)

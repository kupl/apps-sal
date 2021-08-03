n, k = list(map(int, input().split()))
h = sorted(list(map(int, input().split())))

if k == 0:
    print((sum(h)))
else:
    print((sum(h[:-k])))

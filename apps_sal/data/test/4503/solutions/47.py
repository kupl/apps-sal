(h, n) = map(int, input().split())
l = list(map(int, input().split()))
if h - sum(l) <= 0:
    print('Yes')
else:
    print('No')

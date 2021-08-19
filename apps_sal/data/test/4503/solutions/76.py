(h, n) = map(int, input().split())
d = list(map(int, input().split()))
if h - sum(d) <= 0:
    print('Yes')
else:
    print('No')

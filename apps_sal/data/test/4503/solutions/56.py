(h, m) = map(int, input().split())
a = list(map(int, input().split()))
if h - sum(a) > 0:
    print('No')
else:
    print('Yes')

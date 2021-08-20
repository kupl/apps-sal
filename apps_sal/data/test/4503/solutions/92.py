(h, n) = map(int, input().split())
a = list(map(int, input().split()))
x = sum(a)
if h - x <= 0:
    print('Yes')
else:
    print('No')

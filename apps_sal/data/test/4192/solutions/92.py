d, t, s = list(map(int, input().split()))

if d - (t * s) <= 0:
    print('Yes')
else:
    print('No')

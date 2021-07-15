d, s, t = list(map(int, input().split()))

time = d / s
if (time > t):
    print('No')
else:
    print('Yes')

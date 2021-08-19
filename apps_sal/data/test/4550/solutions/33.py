x = list(map(int, input().split()))
y = sorted(x)
if y[0] + y[1] == y[2]:
    print('Yes')
else:
    print('No')

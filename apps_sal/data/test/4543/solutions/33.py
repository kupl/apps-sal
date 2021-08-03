a, b = list(map(str, input().split()))
x = int(a + b)**0.5

if x - int(x) == 0:
    print('Yes')
else:
    print('No')

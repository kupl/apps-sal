l = list(map(int, input().split()))
n = len(set(l))
if n == 2:
    print('Yes')
else:
    print('No')

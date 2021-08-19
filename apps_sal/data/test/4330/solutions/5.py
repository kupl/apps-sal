(a, b) = map(int, input().split())
k = max(a, b) - (max(a, b) - min(a, b)) / 2
if k.is_integer():
    print(int(k))
else:
    print('IMPOSSIBLE')

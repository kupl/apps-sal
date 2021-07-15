a, b = map(int, input().split())
k = (a * a - b * b) / (2 * a - 2 * b)
if k == int(k):
    print(int(k))
else:
    print('IMPOSSIBLE')

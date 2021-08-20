(a, b) = list(map(int, input().split()))
c = (max(a, b) - min(a, b)) / 2
if c == int(c):
    print(int(min(a, b) + c))
else:
    print('IMPOSSIBLE')

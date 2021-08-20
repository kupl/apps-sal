(n, m, x, y) = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
isWar = True
z = min(y_list)
if x < z <= y and max(x_list) < z:
    isWar = False
if isWar:
    print('War')
else:
    print('No War')

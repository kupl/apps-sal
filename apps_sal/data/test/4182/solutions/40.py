(_, _, X, Y) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x_max = max(x)
y_min = min(y)
flag = False
for z in range(X + 1, Y + 1):
    if x_max < z <= y_min:
        flag = True
print('No War' if flag else 'War')

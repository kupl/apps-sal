(n, m, X, Y) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort(reverse=True)
y.sort()
flag = 0
for i in range(X + 1, Y + 1):
    if x[0] < i and y[0] >= i:
        flag = 1
        break
    else:
        flag = 0
if flag == 1:
    print('No War')
else:
    print('War')

n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for z in range(X+1, Y):
    if max(x) < z <= min(y):
        print('No War')
        return
print('War')

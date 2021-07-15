N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for z in range(-100, 101):
    if max(max(x), X) < z and z <= min(min(y), Y):
        print('No War')
        break
else:
    print('War')

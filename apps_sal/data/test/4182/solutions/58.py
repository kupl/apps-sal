n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = sorted(x)
y = sorted(y)

if x[-1] < y[0] and X < x[-1] and y[0] <= Y:
    print("No War")
else:
    print("War")

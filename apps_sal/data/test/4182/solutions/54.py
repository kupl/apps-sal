N,M,X,Y = list(map(int, input().split()))

x = list(map(int, input().split()))
y = list(map(int, input().split()))

Z = [X+1, Y]

x.sort()
y.sort()

Z[0] = max(x[-1]+1, Z[0])
Z[1] = min(y[0], Z[1])

print(("No War" if Z[0]<=Z[1] else "War"))


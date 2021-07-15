N,M,X,Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if (X < Y)&(max(x) < min(y))&(max(x) < Y)&(X < min(y)):
    print("No War")
else:
    print("War")

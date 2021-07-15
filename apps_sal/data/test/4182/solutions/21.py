n,m,x,y = list(map(int, input().split()))
a = list(map(int, input().split())) + [x]
b = list(map(int, input().split())) + [y]
print(("No War" if max(a) < min(b) else "War"))



n, m, X, Y=map(int, input().split())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
x.sort()
y.sort()

Z_start=x[-1]+1
Z_end=y[0]

for z in range(Z_start, Z_end+1):
    if X<z<=Y:
        print("No War")
        return

print("War")

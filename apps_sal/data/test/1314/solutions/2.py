n = int(input())
X = 0
Y = 0
for _ in range(2*n):
    x,y = [int(x) for x in input().split()]
    X += x
    Y += y

print(X//n,Y//n)

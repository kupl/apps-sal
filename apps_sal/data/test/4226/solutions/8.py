X,Y = list(map(int, input().split()))

for i in range(X+1):
    if(Y == 4 * X - (2 * i)):
        print("Yes")
        return

print("No")

x = [0] * 3
y = [0] * 3
for i in range(3):
    x[i], y[i] = map(int,input().split())

if x[0] == x[1] == x[2] or y[0] == y[1] == y[2]:
    print(1)
elif x[0] == x[1] and (y[2]>=max(y[0],y[1]) or y[2]<=min(y[0],y[1])): print(2)
elif x[0] == x[2] and (y[1]>=max(y[0],y[2]) or y[1]<=min(y[0],y[2])): print(2)
elif x[1] == x[2] and (y[0]>=max(y[1],y[2]) or y[0]<=min(y[1],y[2])): print(2)
elif y[0] == y[1] and (x[2]>=max(x[0],x[1]) or x[2]<=min(x[0],x[1])): print(2)
elif y[0] == y[2] and (x[1]>=max(x[0],x[2]) or x[1]<=min(x[0],x[2])): print(2)
elif y[1] == y[2] and (x[0]>=max(x[1],x[2]) or x[0]<=min(x[1],x[2])): print(2)

else: print(3)


X = list(map(int,input().split()))
X.sort(reverse=True)

A,B,C = X[0],X[1],X[2]
P,Q = X[0]-X[1],  X[0]-X[2]
dam = P + Q

if dam%2==0:
    if P%2==0 and Q%2==0:
        out = dam//2
    else:
        out = (dam-2)//2 +1
else:
    out = (dam-1)//2 +2
print(out)


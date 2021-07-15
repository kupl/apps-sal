N = 12
Parent = [I for I in range(N+1)]
Rank = [0]*(N+1)
def FindParent(X):
    if Parent[X]==X:
        return X
    else:
        Parent[X] = FindParent(Parent[X])
        return Parent[X]

def CheckParent(X,Y):
    return FindParent(X)==FindParent(Y)

def UniteParent(X,Y):
    X = FindParent(X)
    Y = FindParent(Y)
    if X==Y:
        return 0
    if Rank[X]<Rank[Y]:
        Parent[X] = Y
    else:
        Parent[Y] = X
        if Rank[X]==Rank[Y]:
            Rank[X] += 1
            
for GA in [3,5,7,8,10,12]:
    UniteParent(1,GA)
for GB in [6,9,11]:
    UniteParent(4,GB)
X,Y = (int(T) for T in input().split())
print(['No','Yes'][CheckParent(X,Y)])

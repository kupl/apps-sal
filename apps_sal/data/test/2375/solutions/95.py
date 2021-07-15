X,Y=map(int,input().split())
if X<Y:
    X,Y=Y,X
    
print('Brown' if (X-1<=Y and Y<=X+1) else 'Alice')

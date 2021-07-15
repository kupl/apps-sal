a,b=map(int,input().split())

def culc(x):
    if x%4==0:
        return x
    elif x%4==1:
        return 1
    elif x%4==2:
        return x+1
    else:
        return 0


print(culc(a-1)^culc(b))

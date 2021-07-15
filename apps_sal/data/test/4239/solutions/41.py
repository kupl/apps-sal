n=int(input())
import bisect
l=[1,6,9,36,81,216,729,1296,6561,7776,46656,59049]
def draw(x,y):
    ind=bisect.bisect_right(l,x)-1
    if ind==0:
        return y+x
    else:
        y += 1
        x1=x-l[ind]
        x2=x-l[ind-1]
        if x1==0 or x2==0:
            return y
        else:
            return(min(draw(x1,y),draw(x2,y)))
print(draw(n,0))

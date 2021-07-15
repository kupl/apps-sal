import math
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def flag(mid):
    count = 0
    for a0 in a:
        count += math.ceil(a0/mid)-1
    if count <= k:
        return True
    else:
        return False
        
def cal(i, j):

    while abs(i-j) > 1:
        mid = (i+j)//2
        if flag(mid):
            j = mid
        else:
            i = mid
    print(j)
    
cal(0, max(a))    


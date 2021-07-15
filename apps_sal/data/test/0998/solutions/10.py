#
n, x  = list(map(int, input().split()))

def creat(n, x):
    if x > 2**n:
        arr = [i for i in range(1, 2**n)]
        return arr
        
    used  = {i:False for i in range(1, 2**n)}
    arr   = []

    for i in range(1, 2**n):
        if i == x:continue
        if used[i] == True: continue
        used[i]    = True    
        used[i^x]  = True
        arr.append(i)
    
    return arr

a  = creat(n, x)
if len(a) == 0:
    print(0)
else:    
    a_ = [a[0]] 
    a_.extend([u ^ v for u, v in zip(a[1:], a[:-1])])

    print(len(a_))
    print(' '.join([str(i) for i in a_]))   



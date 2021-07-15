import math 
 
def div(k):
    res = []
    for i in range(1,int(math.sqrt(k))+2):
        if k % i == 0:
            res.append(i)
    return res
            
t = int(input())
for i in range(t):
    x = int(input())
    if x == 0:
        print("1 1")
    elif x == 1:
        print(-1)
    else:    
        flag = False
        di = div(x)
        for d in di:
            a = x // d
            if ((a+d) % 2 == 0) and (a > d):
                n = (a+d)//2
                lower = (a+d) / (a-d+2)
                upper = (a+d) / (a-d)
                if int(lower) < int(upper):
                    m = int(upper)
                    res = [n,m]
                    flag = True
                    break
        if flag == True:
            print(' '.join(map(str, res)))
        else:
            print(-1)


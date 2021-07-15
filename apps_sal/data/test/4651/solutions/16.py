def doit(lst):
   # print(lst)
    n = len(lst)
    if(n<=1):
        return(lst)
    index = lst.index(min(lst))
    if(index==0):
        l = doit(lst[1:])
        return([lst[0]]+l)
    temp = [lst[index-1]]+lst[index+1:]
    
    return([lst[index]] + lst[:index-1]+doit(temp))

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(*doit(lst))
    
    


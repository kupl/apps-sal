def n_sum(n):
    myList = [int(i) for i in range(1,n+1)]
    return sum(myList)
    
a,b = map(int,input().split())
print(n_sum(b-a)-b)

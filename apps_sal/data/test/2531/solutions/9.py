def func(A, arr_size, val): 
      
    # sort the array 
    A.sort()
    l = 0
    r = arr_size-1
      
    # traverse the array for the two elements 
    while l<r: 
        if (A[l] + A[r] == val): 
            return 1
        elif (A[l] + A[r] < val): 
            l += 1
        else: 
            r -= 1
    return 0
    
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        x=int(input())
        arr.append(x)
    cnt=0
    
    if(n==1):
        print(1)
    else:
        for i in range(n):
            #print(arr)
            x=func(arr, n, arr[i]*2)
            if(x==1):
                cnt+=1
        
        print(cnt)
    
main()

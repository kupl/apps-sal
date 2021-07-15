def getNum(n, arr):
    st1 = []
    st2 = []
    worth = 0
    count = 0
    
    for i in range(n):
        if arr[i] <= worth:
            worth += 1
        else:
            st1.append(arr[i])
    
    if len(st1) == 0:
        return count
    
    count += 1
    while len(st1) != 0:
        if st1[-1] <= worth:
            st1.pop()
            worth += 1
        else:
            st2.append(st1.pop())
        
        if len(st1) == 0:
            if len(st2) == 0:
                return count
            
            st1 = st2
            st2 = []
            count += 1
    
    return count
    
    
n = int(input())

arr = list(map(int, input().split()))

print(getNum(n, arr))

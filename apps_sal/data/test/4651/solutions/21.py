def optimize(arr, idx):
    if idx >= len(arr):
        return
    min_idx = -1
    min_val = 1e9
    for i in range(idx, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    

    for i in range(min_idx-1, idx-1,-1):
        tmp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=tmp
    
    if min_idx == idx:
        min_idx += 1        
    optimize(arr,min_idx)

q=int(input())
for t in range(q):
    n=int(input())
    a=[int(x) for x in input().split()]
    optimize(a,0)
    print(*a)


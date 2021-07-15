T = int(input()) 
for _ in range (T): 

    n,k = map(int, input().split()) 
    A = list(map(int, input().split())) 
    B = list(map(int, input().split())) 
    A.sort() 
    B.sort() 
    for i in range (k): 
        A[i] = max (A[i], B[n-i-1]) 
    print (sum(A)) 

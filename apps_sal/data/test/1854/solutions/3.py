def solve():
    N = int(input())
    A = [int(k) for k in input().split()]
    
    sumA = sum(A)
    
    if sumA < 2*N - 2:
        print ("NO")
        return
    
    ones = []
    
    for i in range(N):
        if A[i] == 1:
            A[i] = 0
            ones.append(i)
            
    t = len(ones)
    dm = (N - t) - 1 + min(2, t)
    
    results = []
    results.append("YES " + str(dm))    
    results.append(str(N-1))
    
    lst = -1
    if t > 0:
        lst = ones[-1]
        ones.pop()
        
    for i in range(N):
        if A[i] > 1:
            if lst != -1:
                A[lst] -= 1
                A[i] -= 1
                results.append(str(lst + 1) + " " + str(i + 1))
            
            lst = i
            
    for i in range(N-1, -1, -1):
        while ones and A[i] > 0:
            A[i] -= 1
            results.append(str(i + 1) + " " + str(ones[-1] + 1))
            ones.pop()
    
    print ('\n'.join(k for k in results))

def __starting_point():
    solve()
__starting_point()

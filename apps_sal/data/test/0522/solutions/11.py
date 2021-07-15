def mat_mul(A,B,m):
    C = [[0]*3 for i in range(3)]
    
    for i in range(3):
        for j in range(3):
            C[i][j] = (A[i][0]*B[0][j]%m + A[i][1]*B[1][j]%m + A[i][2]*B[2][j]%m)%m
    return C

def vec_mul(A,x,m):
    b = [0]*3
    
    for i in range(3):
        b[i] = (A[i][0]*x[0]%m + A[i][1]*x[1]%m + A[i][2]*x[2]%m)%m

    return b
      

def calc_tribonacci(M,n,m,start):
    X = []
    X.append(M[0].copy());X.append(M[1].copy());X.append(M[2].copy())
    R = [[1,0,0],[0,1,0],[0,0,1]]
    while n>0:
        if n%2 == 1:
            R = mat_mul(X,R,m)
        
        X = mat_mul(X,X,m)
        
        n=n//2

    return vec_mul(R, start,m)[2]

def calc_exponent(a,b,m):
    x = a
    r = 1
    while b>0:
        
        if b%2==1:
            r = r*x%m
        
        x = x*x%m
        
        b = b//2
        
    return r

m = 1000000007

n,f1,f2,f3,c = [int(i) for i in input().split()]

M = [[1,1,1],[1,0,0],[0,1,0]]

temp1 = 3*calc_tribonacci(M, n-1, m-1, [1,1,0])

temp1 = (temp1 - calc_tribonacci(M, n-4, m-1, [1,1,0]) - n)%(m-1)

temp2 = calc_tribonacci(M, n-3, m-1, [2,1,1])

temp3 = calc_tribonacci(M, n-3, m-1, [2,1,0])

temp4 = calc_tribonacci(M, n-3, m-1, [1,1,0])

ans = calc_exponent(c, temp1, m)

ans = (ans*calc_exponent(f3, temp2, m))%m

ans = (ans*calc_exponent(f2, temp3, m))%m

ans = (ans*calc_exponent(f1, temp4, m))%m

#print(temp1, temp2, temp3 , temp4)

print(ans)






        


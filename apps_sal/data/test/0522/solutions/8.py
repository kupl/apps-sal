mod = 1000000007

X = [[1,1,1],
    [1,0,0],
    [0,1,0]]

def mul(A, B):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) % ( mod-1 ) for Y_col in zip(*B)] for X_row in A]

def pow_n(A, n):
    if n == 1:
        return A
    
    A_ = pow_n(A, n // 2)
             
    if n % 2 == 0:
        return A_ * A_ % mod 
    else:
        return A_ * A_ * A % mod

def pow_m(A, n):
    if n == 1:
        return A
    
    A_ = pow_m(A, n // 2)
             
    if n % 2 == 0:
        return mul(A_, A_)
    else:
        return mul(mul(A_, A_), A)     
             
n , f1, f2, f3, c = map(int, input().split())
u1  = c * f1 % mod
u2  = (c ** 2) * f2 % mod
u3  = (c ** 3) * f3 % mod
X_  = pow_m(X, n-3)
u_n = pow_n(u3, X_[0][0]) * pow_n(u2, X_[0][1]) * pow_n(u1, X_[0][2]) % mod 
f_n = pow_n(pow_n(c, mod-2), n) * u_n % mod
print(f_n)

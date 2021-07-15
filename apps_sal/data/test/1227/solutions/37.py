N = int(input())
K = int(input())

def pow(a,n):
    ans = 1
    while n > 1:
        if bin(a&1)==bin(1):
            ans = ans*a
        a = a*a
        n = n>>1
    return ans

def com(N,k):
    if k<0 or k>N: return 0
    if k==1:return N
    elif k==2: return N*(N-1)//2
    else: return N*(N-1)*(N-2)//6

S = len(str(N))
N = str(N)
def helper(i,k,smaller):
    if i==S:
        if k==0: return 1
        else: return 0
    if k ==0: return 1
    if smaller: return com(S-i,k)*(9**k)
    else:
        if N[i]=='0': return helper(i+1,k,False)
        else:
            zero = helper(i+1,k,True)
            a = helper(i+1,k-1,True)*(int(N[i])-1)
            b = helper(i+1,k-1,False)
            return zero + a + b
print((helper(0,K,False)))


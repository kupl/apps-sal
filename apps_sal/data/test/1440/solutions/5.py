N = int(input())
A = [int(a) for a in input().split()]
s = sum(A)
r = 0
k = N

def nextk(f = 1):
    nonlocal k
    if f and k >= 0:
        A[k] = 0
    k -= 1
    while k >= 0 and A[k] != 1:
        k -= 1
    
def ct(n):
    if n % 2 == 0:
        return n//2
    return (n-3)//2

nextk(0)
for i in range(N)[::-1]:
    if k < 0:
        break
    
    j = 0
    if A[i] == 1:
        r += 1
        if k == i:
            nextk(0)
    else:
        j = ct(A[i])
        
        while j > 0:
            nextk()
            j -= 1
print((s-r)//3)


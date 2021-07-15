import math
n = int(input())
sq = int(math.sqrt(n))

M = {}

M[1] = 1
M[n*(n+1)//2] = 1

for i in range(2, sq+1):
    if n%i == 0:
        r = n-i+1
        ret = ((1+r)*(r-1+i))//(2*i)
        M[ret]=1

        if (n//i != sq):
            f = n//i
            r = n-f+1
            ret = ((1+r)*(r-1+f))//(2*f)
            M[ret]=1

ret = sorted(M.keys())

print(*ret)

import math
n = int(input())
s = int(input())
def solve(n, s):
    if n == s:
        return n+1
    for b in range(2, math.floor(n**0.5)+1):
        tmp = n
        res = 0
        while tmp>=b:
            res+=tmp%b
            tmp //=b
        res += tmp
        if res == s:
            return b
    for p in range(int(n**0.5), 0, -1):
        r = s-p
        if r<0:
            continue
        if (n-r)%p == 0:
            b = (n-r)//p
            if r<b and b*b>n:
                return b
    return -1
print(solve(n, s))

import sys
sys.setrecursionlimit(10**5)
N, X = map(int,input().split())
l = [1]
for i in range(N):
    l.append(2*l[-1]+3)
d = {}
def f(n,x):
    if (n,x) in d:
        return d[(n,x)]
    if n == 0:
        ans = 1
    elif x == 1:
        ans = 0
    elif x <= l[n-1]+1:
        ans = f(n-1,x-1)
    elif x == l[n-1]+2:
        ans = f(n-1,l[n-1])+1
    elif x <= 2*l[n-1]+2:
        ans = f(n-1, l[n-1])+1+f(n-1, x-l[n-1]-2)
    else:
        ans = 2*f(n-1, l[n-1])+1
    d[(n,x)] = ans
    return ans
print(f(N, X))
